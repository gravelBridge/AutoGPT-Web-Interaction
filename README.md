# AutoGPT Web Interaction Plugin

![Screenshot 2023-05-01 at 7 37 16 PM](https://user-images.githubusercontent.com/107640947/235567612-0fd49909-197c-4ebf-9f7f-8edf1bf4d7d0.png)

The AutoGPT Web Interaction Plugin enables Auto-GPT to interact with websites.

Note: The plugin is very flakey on GPT-3.5, I recommend using GPT-4. However, it can still perform basic tasks on GPT-3.5.

## Key Features:
- Allows Auto-GPT to click elements.
- Allows Auto-GPT to type text.
- Allows Auto-GPT select elements.
- Brings Auto-GPT to scroll

## Installation

Follow these steps to configure the Auto-GPT Email Plugin:

### 1. Clone this repository.

### 2. cd into the directory, and run pip install -r requirements.txt

### 3. Zip/Compress the web_interaction folder

### 4. Drag the new zip file into the Auto-GPT plugins folder.

### 5. Set `ALLOWLISTED_PLUGINS=AutoGPTWebInteraction,example-plugin1,example-plugin2,etc` in your AutoGPT `.env` file.

### 6. Edit goals
When using Auto-GPT please set one of the goals to "Remember to use the Web Interaction Plugin possible".
