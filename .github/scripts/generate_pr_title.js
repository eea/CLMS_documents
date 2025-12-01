// Generate descriptive PR title based on changed files
// Usage: Called from GitHub Actions with context

module.exports = async ({ github, context, core, version }) => {
  const pr = context.payload.pull_request;
  if (!pr) {
    core.setFailed("No PR context found.");
    return;
  }

  const base = pr.base.ref;
  const head = pr.head.ref;

  // Define semantic-release type and scope
  const typeMap = {
    test: "feat",
    main: "release",
  };
  const type = typeMap[base] || "chore";

  // Get changed files to make title more descriptive
  const { data: files } = await github.rest.pulls.listFiles({
    owner: context.repo.owner,
    repo: context.repo.repo,
    pull_number: pr.number,
  });

  // Count only .qmd documentation changes (ignore media files)
  const docsFiles = files.filter((f) => f.filename.startsWith("DOCS/") && f.filename.endsWith(".qmd"));

  // Group by category (first directory after DOCS/)
  const categories = {};
  docsFiles.forEach((f) => {
    const match = f.filename.match(/^DOCS\/([^/]+)\//);
    if (match) {
      const category = match[1];
      categories[category] = (categories[category] || 0) + 1;
    }
  });

  // Build descriptive content from categories
  const categoryList = Object.entries(categories)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([cat, count]) => {
      const formatted = cat.replace(/_/g, " ");
      return count > 1 ? `${count} ${formatted}` : formatted;
    });

  // Construct title
  let title;
  if (categoryList.length > 0) {
    const what = categoryList.slice(0, 3).join(", "); // Max 3 categories in title
    const more = categoryList.length > 3 ? ` +${categoryList.length - 3} more` : "";
    title = `${type}(docs): update ${what}${more}`;
  } else {
    // Fallback to branch-based title
    title = `${type}(merge): promote ${head} to ${base}`;
  }

  // Truncate to 100 characters safely
  if (title.length > 100) {
    title = title.slice(0, 97) + "...";
  }

  console.log(`Setting PR title to: ${title}`);

  await github.rest.pulls.update({
    owner: context.repo.owner,
    repo: context.repo.repo,
    pull_number: pr.number,
    title: title,
  });
};
