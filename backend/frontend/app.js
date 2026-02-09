function fillIdea(text) {
  document.getElementById("idea").value = text;
}

/* ---------- Helper: Safe formatting ---------- */
function formatText(text) {
  if (!text || text === "undefined" || text === null) {
    return "Not available";
  }
  return text.toString().replace(/\n/g, "<br>");
}

/* ---------- Start Project ---------- */
async function start() {
  const idea = document.getElementById("idea").value.trim();
  const output = document.getElementById("output");
  const loading = document.getElementById("loading");
  const steps = document.getElementById("steps");
  const layout = document.querySelector(".layout");
  layout.classList.remove("full");

  if (!idea) {
    output.innerText = "⚠️ Please enter an idea first.";
    return;
  }

  // Reset UI
  output.innerHTML = "";
  loading.classList.remove("hidden");

  steps.classList.remove("hidden");
  [...steps.children].forEach(s => s.classList.remove("active"));

  setTimeout(() => steps.children[0]?.classList.add("active"), 400);
  setTimeout(() => steps.children[1]?.classList.add("active"), 1800);
  setTimeout(() => steps.children[2]?.classList.add("active"), 3200);

  try {
    const res = await fetch("/start", "/projects" , {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea })
    });

    const data = await res.json();
    loading.classList.add("hidden");
    

    // If idea unclear
    if (!data.is_clear) {
      output.innerHTML = `
        <div class="card">
          <h3>❓ More details needed</h3>
          <p>${formatText(data.questions)}</p>
        </div>
      `;
      return;
    }
    
    layout.classList.add("full");

output.innerHTML = `
<div class="card top-actions">
  <button class="new-idea-btn" onclick="resetToInput()">➕ New Idea</button>
  <button class="secondary" onclick="downloadProject()">⬇ Download</button>
</div>

<div class="tabs">
  <button class="tab active" onclick="openTab(event, 'ideaTab')">Overview</button>
  <button class="tab" onclick="openTab(event, 'featuresTab')">Features</button>
  <button class="tab" onclick="openTab(event, 'roadmapTab')">Roadmap</button>
  <button class="tab" onclick="openTab(event, 'techTab')">Tech Stack</button>
  <button class="tab" onclick="openTab(event, 'marketTab')">Market</button>
</div>

<div id="ideaTab" class="tab-content active">
  <h3>✅ Refined Idea</h3>
  <pre>${(data.refined_idea || "Not available").replace(/\\n/g, "\n")}</pre>
  <button class="copy-btn" onclick="copyText(\`${data.refined_idea || ""}\`)">Copy</button>
</div>

<div id="featuresTab" class="tab-content">
  <h3>📋 Features</h3>
  <pre>${(data.features || "Not available").replace(/\\n/g, "\n")}</pre>
  <button class="copy-btn" onclick="copyText(\`${data.features || ""}\`)">Copy</button>
</div>

<div id="roadmapTab" class="tab-content">
  <h3>🛣️ Roadmap</h3>
  <pre>${(data.roadmap || "Not available").replace(/\\n/g, "\n")}</pre>
  <button class="copy-btn" onclick="copyText(\`${data.roadmap || ""}\`)">Copy</button>
</div>

<div id="techTab" class="tab-content">
  <h3>⚙️ Recommended Tech Stack</h3>
  <pre>${(data.techstack || "Not available").replace(/\\n/g, "\n")}</pre>
  <button class="copy-btn" onclick="copyText(\`${data.techstack || ""}\`)">Copy</button>
</div>

<div id="marketTab" class="tab-content">
  <h3>Market Analysis</h3>
  <pre>${(data.market_analysis || "Not available").replace(/\\n/g, "\n")}</pre>
  <button class="copy-btn" onclick="copyText(\`${data.market_analysis || ""}\`)">Copy</button>
</div>
`;


  } catch (err) {
    loading.classList.add("hidden");
    output.innerHTML = `
      <div class="card">
        <h3>❌ Error</h3>
        <p>Backend error. Check terminal logs.</p>
      </div>
    `;
  }
}

/* ---------- Load Saved Projects ---------- */
async function loadProjects() {
  const projects = document.getElementById("projects");
  projects.innerText = "Loading projects...";

  try {
    const res = await fetch("http://127.0.0.1:8000/projects");
    const data = await res.json();

    if (!data.length) {
      projects.innerText = "No saved projects yet.";
      return;
    }

    projects.innerHTML = data.map(p => `
      <div class="card">
        <strong>📌 Project #${p.id}</strong>
        <p>${p.user_idea}</p>
      </div>
    `).join("");

  } catch {
    projects.innerText = "❌ Failed to load projects.";
  }
}

/* ---------- Reset to Input View ---------- */
function resetToInput() {
  const layout = document.querySelector(".layout");
  const output = document.getElementById("output");
  const steps = document.getElementById("steps");
  const loading = document.getElementById("loading");

  // Show left panel again
  layout.classList.remove("full");

  // Clear output
  output.innerHTML = "";

  // Hide steps and loader
  steps.classList.add("hidden");
  loading.classList.add("hidden");

  // Optional: clear textarea
  document.getElementById("idea").value = "";
}

/* ---------- Tabs ---------- */
function openTab(evt, tabId) {
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));

  evt.currentTarget.classList.add("active");
  document.getElementById(tabId).classList.add("active");
}

/* ---------- Copy ---------- */
function copyText(text) {
  navigator.clipboard.writeText(text);
  alert("Copied!");
}

/* ---------- Download ---------- */
function downloadProject() {
  const content = document.getElementById("output").innerText;
  const blob = new Blob([content], { type: "text/plain" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "FoundryAI_Project.txt";
  a.click();
}
