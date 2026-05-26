const http = require("http");
const fs = require("fs");
const path = require("path");

// load .env file if present
if (fs.existsSync(path.join(__dirname, ".env"))) {
  fs.readFileSync(path.join(__dirname, ".env"), "utf8")
    .split("\n")
    .forEach((line) => {
      const [key, ...val] = line.split("=");
      if (key && val.length) process.env[key.trim()] = val.join("=").trim();
    });
}

const PORT = 3000;
const API_KEY = process.env.GROQ_API_KEY;

async function handleChat(req, res) {
  let body = "";
  req.on("data", (chunk) => (body += chunk));
  req.on("end", async () => {
    const { message } = JSON.parse(body);

    if (!API_KEY) {
      res.writeHead(500, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ error: "GROQ_API_KEY not set" }));
    }

    try {
      const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${API_KEY}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          model: "llama-3.3-70b-versatile",
          messages: [
            {
              role: "system",
              content: "You are Botsolver, a helpful assistant. Keep responses clear and concise.",
            },
            { role: "user", content: message },
          ],
        }),
      });

      const data = await response.json();
      const reply = data.choices[0].message.content;
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ reply }));
    } catch (err) {
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: err.message }));
    }
  });
}

const server = http.createServer((req, res) => {
  if (req.method === "POST" && req.url === "/api/chat") {
    return handleChat(req, res);
  }

  const filePath = path.join(__dirname, "index.html");
  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      return res.end("Not found");
    }
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`Botsolver running at http://localhost:${PORT}`);
});
