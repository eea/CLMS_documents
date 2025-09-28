#!/usr/bin/env node
const sharp = require("sharp");
const { mathjax } = require("mathjax-full/js/mathjax.js");
const { TeX } = require("mathjax-full/js/input/tex.js");
const { SVG } = require("mathjax-full/js/output/svg.js");
const { liteAdaptor } = require("mathjax-full/js/adaptors/liteAdaptor.js");
const { RegisterHTMLHandler } = require("mathjax-full/js/handlers/html.js");
const { AllPackages } = require("mathjax-full/js/input/tex/AllPackages.js");

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const tex = new TeX({ packages: AllPackages });
const svg = new SVG({ fontCache: "none" });
const html = mathjax.document("", { InputJax: tex, OutputJax: svg });

let input = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", chunk => (input += chunk));
process.stdin.on("end", async () => {
  const display = process.argv.includes("--display");
  const node = html.convert(input.trim(), { display });
  const svgOutput = adaptor.innerHTML(node);

  try {
    // Render at high density (DPI)
    const pngBuffer = await sharp(Buffer.from(svgOutput))
      .png()
      .resize({ width: 2000 })   // force 2000px wide (scale up math)
      .toBuffer();
    process.stdout.write(pngBuffer);
  } catch (err) {
    console.error("Sharp conversion error:", err);
    process.exit(1);
  }
});
