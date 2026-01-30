# Choosing the Right LLM
### How to select, train and apply state-of-the-art LLMs to real-world business use cases.

![Choosing the right LLM](assets/pickme.png)

This repo has companion code for my class on comparing and training LLMs.

### Resources to accompany the class

The resources are [here](https://edwarddonner.com/2024/06/26/choosing-the-right-llm-resources/)

### A note before you begin

I'm here to help you be most successful with your learning! If you hit any snafus, or if you have any ideas on how I can improve the course, please do reach out in the platform or by emailing me direct (ed@edwarddonner.com). It's always great to connect with people on LinkedIn to build up the community - you'll find me here:  
https://www.linkedin.com/in/eddonner/

If you'd like to go more deeply into LLMs and Agents:
- I have a [program of intensive courses on LLM Engineering and Agents](https://edwarddonner.com/curriculum/) with 20+ weeks of courses  
- My [Proficient AI Engineer Program](https://edwarddonner.com/proficient/)
- I'm running a number of [Live Events](https://edwarddonner.com/2025/11/11/ai-live-event/) with O'Reilly and Pearson

## For those that use GitHub Codespaces

GitHub codespaces users can use this to launch a codespace for this repo.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ed-donner/choose_llm?quickstart=1)

## For the introduction section - using Ollama

In the first section, we use Ollama to run a model locally
1. Download and install Ollama from https://ollama.com noting that on a PC you might need to have administrator permissions for the install to work properly
2. On a PC, start a Command prompt / Powershell (Press Win + R, type `cmd`, and press Enter). On a Mac, start a Terminal (Applications > Utilities > Terminal).
3. Run `ollama run llama3.2` or for smaller machines try `ollama run llama3.2:1b`
4. If this doesn't work, you may need to run `ollama serve` in another Powershell (Windows) or Terminal (Mac), and try step 3 again
5. And if that doesn't work on your box, I've set up this on the cloud. This is on Google Colab, which will need you to have a Google account to sign in, but is free:  https://colab.research.google.com/drive/1-_f5XZPsChvfU1sJ0QqCePtIuc55LSdu?usp=sharing

Any problems, please contact me!

Now on to the main setup:

## Setup instructions

Hopefully I've done a decent job of making these guides bulletproof - but please contact me right away if you hit roadblocks:

[Setup Instructions](setup/SETUP-new.md)

### An important point on API costs (which are optional! No need to spend if you don't wish)

During this example project, I'll suggest you try out the leading models at the forefront of progress, known as the Frontier models. These services have some charges, but I'll keep cost minimal - like, a few cents at a time. And I'll provide alternatives if you'd prefer not to use them.

Please do monitor your API usage to ensure you're comfortable with spend; I've included links below. There's no need to spend anything more than a couple of dollars. Some AI providers such as OpenAI require a minimum credit like \$5 or local equivalent; we should only spend a fraction of it, and you'll have plenty of opportunity to put it to good use in your own projects. But it's not necessary in the least; the important part is that you focus on learning.

### The most important part

The best way to learn is by **DOING**. I don't type all the code during the workshop; I execute it for you to see the results. You should work through afterwards, running each cell, inspecting the objects to get a detailed understanding of what's happening. Then tweak the code and make it your own.

### Monitoring API charges

You can keep your API spend very low; you can monitor spend at the dashboards: [here](https://platform.openai.com/usage) for OpenAI, [here](https://console.anthropic.com/settings/cost) for Anthropic and [here](https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/cost) for Google Gemini.

The charges for the exercises in this course should always be quite low, but if you'd prefer to keep them minimal, then be sure to always choose the cheapest versions of models:
1. For OpenAI: Always use model `gpt-4.1-nano` in the code instead of other models
2. For Anthropic: Always use model `claude-haiku-4-5` in the code instead of the other Claude models

Please do message me or email me at ed@edwarddonner.com if this doesn't work or if I can help with anything. I can't wait to hear how you get on.

<table style="margin: 0; text-align: left;">
    <tr>
        <td style="width: 150px; height: 150px; vertical-align: middle;">
            <img src="assets/resources.jpg" width="150" height="150" style="display: block;" />
        </td>
        <td>
            <h2 style="color:#f71;">Other resources</h2>
            <span style="color:#f71;">I've put together this webpage with useful resources.<br/>
            <a href="https://edwarddonner.com/2024/06/26/choosing-the-right-llm-resources/">https://edwarddonner.com/2024/06/26/choosing-the-right-llm-resources/</a><br/>
            Please keep this bookmarked, and I'll continue to add more useful links there over time.
            </span>
        </td>
    </tr>
</table>
