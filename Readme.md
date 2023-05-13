# Visualizing Relationships in ChatGPT
#### Video Demo:  <URL HERE>
#### Description: Ask ChatGPT for recommendations about various topics and visualize the relationship as a graph.

The idea of this project is to be able to visualize the data relationships inside ChatGPT for a variety of topics. All we have to do is ask it in the right way to get the data out.

How it works.

* The 'download' step asks ChatGPT (via its API) for a list of popular items (80's movies, fast food restaurants, etc). 
  * For each of the original recommendations, the tool asks it what else I might also like that is similar.
* The output is filtered for cruft, cleansed and standardized, then saved as JSON in a common format.  
  * This way it can be cleaned up manually as needed before additional processing. 
  * ChatGPTs responses can be very inconsistent, see more notes below on that.
* The 'build' step loads the JSON, converts into a graph (nodes for things, edges for recommendations) and renders it using a few different strategies.


NOTE: An OpenAI API key is required, **and to get one you have to input a credit card**. However, it is pretty affordable at this scale. So far on this entire project with all the test calls and trial and error I've spent a grand total of just $0.32. 


## List of topics

* _80sMovies_ - what 1980's Movies might I also enjoy?
* _FastFood_ - what Fast Food Restaurants might I also enjoy?
* _PianoPieces_ - what are some good Classical Piano Pieces to study that are related/similar?
* _PrescriptionDrugs_ - what does GPT think people are prescribed in combination the most?


## Command Line Options

`python main.py -command {download, build, etc} -topic {all, or 80sMovies, FastFood, etc)`

**command**
    
* _download_ - gets recommendations from ChatGTP and saves the result as JSON 

The following command options use the downloaded JSON (download must have been run prior):

* _visnetwork_ - build VisNetwork HTML file of the network graph (creates an HTML file you can double click on and play with the network / nodes in your browser) 
* _svg_ - builds an svg of the network graph using the `scikit-network` package
* _cicular_ - builds a png of the network graph using the `networkx.circular_layout`, highlighting the top 3 connected nodes
* _topnodes_ - outputs the top 10 connected nodes in order for the given topic
* _build_ - runs visnetwork, svg, circular, and topnodes

**topic**

* 80sMovies (eighties movies recommendations)
* FastFood  (fast food restaurant recommendations)
* PianoPieces (classical piano piece recommendations)
* PrescriptionDrugs (drugs people taking in combination)
* _all_ (default, runs the command on all topics)

**model**

* _gpt-3.5-turbo_  (default, currently the option supported option)  
  * the plan is to support GPT-4 and other models when they become available


**verbose**

* defaults to true

## User Guide

This project works on Python 3.9.x on my Mac laptop. It should work anywhere Pyton 3.9 runs.

1. Create a Python virtual environment for the project, e.g. `pyenv virtualenv 3.9.9 chatgpt_visualize_relationships`.
2. Create a `.python-version` file in the root of the project with content `chatgpt_visualize_relationships` (or whatever your named your virtual env in step 1).
3. Install dependencies using `pip install -r requirements.txt`.
4. Run `export OPENAI_API_KEY='sk-...'` with your OpenAI API key in your terminal.
5. Run `python main.py -command download` to get all the data as JSON. 
   1. This is the part that talks to the ChatGPT API. 
   2. The API is SLOW, it can take a minute or two per topic to collect the data.
6. Run `python main.py -command build` to build the VisNetwork HTML output and png output.
7. Check out the results in `./out/`
   1. Open the 'view_all.html' file in your browser for a carousel of the results. Works best in full screen.
   2. Open the individual *_pyvis.html files.
9. You may notice duplicate nodes (very similar names).  This happens because ChatGPT has multiple ways of describing the same thing. 
   1. Duplicates can be corrected manually in the JSON files in `./out/` using search and replace.
   2. The concrete Conversations classes have logic to try and address this, but it is not perfect.
   

## Challenges

### Inconsistent Output Format

Initially I tried to get ChatGPT to return JSON. This is really cool when it works. 
You can even tell it the specific format you want and it will do it.

An example prompt:

```
Provide the response in JSON only, following this format:
[{
  "name": {name of the piece},
  "composer": {composer},
  "difficulty_level": {difficulty level}
}, ...]
```


However, in practice using API calls 80% of the time it does it, the other 20% of the time it says something like:

> "Sorry, as an AI language model, I am not able to provide a JSON response only."

This is in spite of the fact that I TOLD IT to return JSON and NOTHING else.
So it acts a bit difficult at times, and you never know which one you will get... which seems very non-computer like but it is designed to vary the output to seem more human like.

For a script like this that makes repeated calls, having the output format alternate between text and json is unacceptable.
So the solution was to tell it to return a plain list.

```
Provide the response with one answer per line, no leading numbers or symbols, and no other commentary
```

This approach provides consistent results of simple lists. 
Sometimes it numbers the items (1., 2., 3...) even when I tell it not to, but there is code in `BaseConversation.clean_line` to address this.

### Topic - Piano Pieces 

Some composers like JS Bach and Mozart have their work organized by a numbering system (BWV and K respectively).
For example Bach's "Sonata in C" could refer to BWV 966 (for Clavier), BWV 1033 (for Flute). So I asked ChatGPT to include these numbers to get better results.

```
for pieces composed by Johann Sebastian Bach include the BWV number after the name of the piece and before the composer's name
for pieces composed by Mozart include the K number after the name of the piece and before the composer's name
```

However, the way ChatGPT formats the responses is all over the place.  With Mozart's Sonata in C K 545 could be returned as (K545), (K.545), and (K 545). Sometimes it puts this information at the end, sometimes before the composer name, etc. The project includes custom code to cleanup these variations.  Still for this particular Conversation class, the JSON needs additional manual cleanup. Without doing this step the visualizations include duplicated nodes which throws everything off.


## Ways to make this project better:

1. Support additional Language Models (LLMs), such as Bard and others.
2. Support the gpt-4 model when it comes out, and compare results.
3. Run it with different 'temperatures' which is a parameter ChatGPT 3.5 offers that tells it how random/risky the response should be. 0 is static, and 1 is the max. Code currently has 1 for temperature, so the results do change from run to run.
4. Add additional conversations, perhaps ones that are more controversial or dig into biases the AI has.
5. Improve the output visualization quality.


## Possible Topics for Later

My goal at this point was to launch the tool with fairly benign topics. Other fun topics might be:

* TV shows from 2010-2020 (or other decades)
* Good places to work
* Rock bands
* Popular careers and related careers
* Programming languages
* Sci-fi books

Many AI researches have discovered clever ways of trick ChatGPT into saying inappropriate things or provide instructions on how to harm others (aka "jail breaking"). For now I stayed away from such topics, but this tool could potentially be used in combination with a jail break to extract noteworthy data.

AI researchers are also interested in what biases are inherent in ChatGPT (racial, gender, cultural, etc). This tool could also be used to help uncover biases in its data relationships.

Here are some example controversial topics that could be added later:

* Street drugs (may take some jail breaking)
* Explosives  (may take some jail breaking)
* Historical figures (see if they are all white men)
* Famous people (see if it is USA centric or includes global celebrities, people of color, etc)
* Travel destinations to safe countries (all white Christian countries?)





