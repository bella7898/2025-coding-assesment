# UAS 2025-26 Software Team Coding Assessment

Welcome to the 2025-26 coding assessment for UBC UAS! This exercise will evaluate your ability to write clean, maintainable code and refactor existing messy code.

## Getting Started

### Step 1: Create a GitHub Account

1. Go to [github.com](https://github.com)
2. Click "Sign up" in the top right corner
3. Create your account with a professional username (e.g., firstname-lastname)
4. Choose the free plan when prompted
5. Verify your email address

### Step 2: Fork This Repository

1. While logged into GitHub, go to the original assessment repository (link provided separately)
2. Click the **"Fork"** button in the top right corner of the repository
3. This creates your own copy of the repository under your GitHub account
4. You should now see the repository under `https://github.com/YOUR_USERNAME/repository-name`

### Step 3: Install GitHub Desktop

#### Windows & Mac

1. Go to [desktop.github.com](https://desktop.github.com)
2. Download and install GitHub Desktop
3. Launch GitHub Desktop
4. Sign in with your GitHub account

#### Linux

GitHub Desktop isn't officially available for Linux, but you can:

- Use git command line (see alternative instructions below)
- Or try the unofficial Linux version at [github.com/shiftkey/desktop](https://github.com/shiftkey/desktop)

### Step 4: Clone Your Fork

#### Using GitHub Desktop (Recommended)

1. Open GitHub Desktop
2. Click "Clone a repository from the Internet"
3. Select your forked repository from the list
4. Choose where to save it on your computer (remember this location!)
5. Click "Clone"

#### Alternative: Using Command Line

```bash
git clone https://github.com/YOUR_USERNAME/repository-name.git
cd repository-name
```

### Step 5: Install Python

#### Windows

1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or newer
3. **Important:** Check "Add Python to PATH" during installation
4. Open Command Prompt and type `python --version` to verify

#### Mac

1. **Option 1 - Official installer:**
   - Go to [python.org](https://www.python.org/downloads/)
   - Download and install Python 3.8 or newer
2. **Option 2 - Using Homebrew (if you have it):**
   ```bash
   brew install python
   ```
3. Verify with `python3 --version` in Terminal

#### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify with `python3 --version`

### Step 6: Running the Code

1. Navigate to your cloned repository folder
2. Open terminal/command prompt in that folder
3. Run the script:
   ```bash
   python calculation.py
   ```
   (On Mac/Linux you might need `python3` instead of `python`)

## Your Assignment

You'll be working with a Python script that converts GPS coordinates for drone navigation. The current code works but is messy and hard to maintain.

### What You'll See Initially

When you first run the script, you'll see:

- Several **FAILED** tests - this is expected!
- The current messy output from `show_drone_locations()`
- Clear error messages showing what's wrong

### Tasks to Complete

#### 1. Implement the Helper Function

- Complete the `convert_to_readable_format()` function
- Follow the step-by-step comments inside the function
- Make the unit tests pass

#### 2. Refactor the Main Function

- Clean up `show_drone_locations()` to use your helper function
- Hint: Variable names are one thing to improve!

#### 3. Verify Your Work

- Run the script again
- All tests should now **PASS**
- The output should be clean and readable

### Success Criteria

Your solution is complete when:

- [ ] All unit tests pass
- [ ] Integration test passes
- [ ] `show_drone_locations()` uses your helper function

### Example of Good Output

## Step 7: Commit and Push Your Changes

### Using GitHub Desktop

1. Open GitHub Desktop
2. You should see your changes listed on the left side
3. Write a clear commit message describing what you did (e.g., "Implement helper function and refactor coordinate conversion")
4. Click "Commit to main"
5. Click "Push origin" to upload your changes to GitHub

### Using Command Line

```bash
git add .
git commit -m "Some commit message here"
git push origin main
```

## Submission

When complete, please share the link of your GitHub repository (your forked version) containing your work in the Google Form submission.

**Your repository link should look like:**
`https://github.com/YOUR_USERNAME/repository-name`

Make sure your repository is **public** so reviewers can access your code.

### Questions?

If you get stuck or have questions, please email:

software@ubcuas.com
