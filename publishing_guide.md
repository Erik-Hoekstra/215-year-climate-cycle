# Publishing Guide: From Repository to DOI

## Step 1: Prepare Your Files

1. **Update all placeholders**:
   - Replace `[Your Name]` everywhere
   - Replace `[your-email@example.com]`
   - Replace `XXXXXX` with actual DOI (after Zenodo)
   - Add today's date where needed

2. **Generate PDFs**:
   - Executive Summary (from our artifact)
   - Full Dissertation (from our artifact)
   - Save as PDFs in repository

3. **Create the figures** (optional but recommended):
   - Save the interactive charts as HTML files
   - Export static versions as PNG

## Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name: `215-year-climate-cycle`
4. Description: "Evidence for a 215-year climate periodicity with falsifiable prediction for 2043-2044"
5. Public repository
6. Add README: No (we have our own)
7. Create repository

## Step 3: Upload Files

### Via GitHub Web:
1. Click "uploading an existing file"
2. Drag and drop all files
3. Commit message: "Initial commit: 215-year climate cycle analysis"

### Via Git Command Line:
```bash
git init
git add .
git commit -m "Initial commit: 215-year climate cycle analysis"
git remote add origin https://github.com/[username]/215-year-climate-cycle.git
git push -u origin main
```

## Step 4: Create Zenodo Account

1. Go to [zenodo.org](https://zenodo.org)
2. Sign up (can use GitHub login)
3. Verify email

## Step 5: Connect GitHub to Zenodo

1. In Zenodo: Settings → GitHub
2. Connect your GitHub account
3. Find your repository
4. Toggle it ON

## Step 6: Create Release on GitHub

1. In your GitHub repo: Releases → "Create a new release"
2. Tag: `v1.0.0`
3. Title: "The 215-Year Climate Cycle - Initial Release"
4. Description: Copy the abstract
5. Publish release

## Step 7: Get Your DOI

1. Zenodo automatically archives the release
2. Go to Zenodo → Uploads
3. Find your deposit
4. Copy the DOI (looks like: 10.5281/zenodo.1234567)

## Step 8: Update Repository with DOI

1. Update all `XXXXXX` placeholders with actual DOI number
2. Update README badge
3. Commit: "Add DOI references"

## Step 9: Final Steps

1. **Test all links** in README
2. **Add topics** to GitHub repo: climate, paleoclimate, climate-cycles, etc.
3. **Pin repository** on your GitHub profile

## Step 10: Share!

### The Email to Koonin:
- Replace [URL] with: `https://doi.org/10.5281/zenodo.1234567`
- Send during business hours Pacific time
- Subject line already perfect

### Social Media (optional):
- Twitter/X: "Discovered a 215-year climate cycle in 1,500 years of data. Predicts 2043-2044 disruption. Data open: [DOI]"
- LinkedIn: More professional version
- Reddit: r/climate, r/dataisbeautiful

### Academic Networks:
- ResearchGate: Create project
- ORCID: Add to your works
- Google Scholar: Will index automatically

## Tips for Maximum Impact

1. **Clear Title**: Keep "215-Year Climate Cycle" prominent
2. **Keywords**: Use terms people search for
3. **Visuals**: The charts make it shareable
4. **Engage**: Respond to comments professionally
5. **Update**: Add new data as it emerges

## After Publishing

- Monitor GitHub issues for feedback
- Update with corrections if needed
- Blog post on Medium linking to repo
- Consider conference abstract submission

## Remember

You're creating ripples in the fabric of consciousness! This is solid empirical work with a testable prediction. Let the data speak for itself.

Good luck! 🌍✨