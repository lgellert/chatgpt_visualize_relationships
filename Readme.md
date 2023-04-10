


## Command Line Options

visualize_gpt -command {command} -topic {all, or eighties, fastfood, etc).   -model (gpt-3.5-turbo, gpt-4)

commands
    download - gets recommendations from ChatGTP and saves the result as JSON
    visnetwork - using the downloaded JSON build VisNetwork HTML file of the network graph (creates an HTML file you can double click on and play with the network / nodes in your browser), requires download task to be executed at least once so JSON results file exists first
    TODO - using the downloaded JSON build png files of the network graph using library XYZ   

    all - runs download, visnetwork, ..

topic
    Eighties     (eighties movies)
    FastFood     (fast food restaurants)
    Classical    (classical piano pieces)
    All (default, runs the command on all topics)

model
gpt-3.5-turbo  (default, currently the option supported option)  put this here to support GPT-4 and later when they are available


## User Guide

This works on Python 3.9.x on my Mac laptop. It should work anywhere Pyton 3.9 runs.

1. Create a Python virtual environment for the project, e.g. `pyenv virtualenv 3.9.9 chatgpt_visualize_relationships`
2. Create a .python-version file in the root of the project with content  chatgpt_visualize_relationships (or whatever your named your virtual env)
3. Install dependencies using `pip install -r requirements.txt`
4. Run `export OPENAI_API_KEY='sk-...'` with your OpenAI API key in your terminal
5. Run `-c download` to get all the data as json
6. Look through the JSON and correct any duplicates. Sometimes ChatGPT will have multiple ways of describing the same thing. The concrete Conversations classes have logic to try and address this, but it is not perfect.
7. Run `-c visnetwork` to build the VisNetwork HTML output
8. Run ....




Ways to make it better:

1. Support additional LLMs (Bard, etc)
2. Support gpt-4 when it comes out, and compare results
3. Add additional conversations, perhaps ones that are more controversial or dig into any biases the AI has.
4. Run it with different 'temperatures' which is a parameter ChatGPT 3.5 offers that tells it how random/risky the response should be. 0 is static, and 1 is the max. Code currently has 0.5 for temperature, so the results do change slighty run to run.
5. Ability to output network graphs side by side, better way of automatically browsing the results.






