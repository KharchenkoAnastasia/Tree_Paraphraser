# Tree_Paraphraser


**Tree_Paraphraser_app.py** is a Python API that implements a single endpoint that accepts an English text syntax tree and returns paraphrased versions of it. 

-path: /paraphrase<br>
-HTTP method: GET<br>
-query parameters:<br>
   -tree: str (required) - syntax tree as a string<br>
    -limit: int (optional, default: 20) - the maximum number of paraphrased tests to return<br>
   -response: list of paraphrased trees in JSON format<br>
   
   <br>
   
   Paraphrasing is done as follows:<br>
1. Find in the test all NP (noun phrases) - noun phrases consisting of several NP separated by tags, (commas) or СС (connected phrases, for example "and").<br>
2. Generate options for exchanging these child NPs with each other.<br>

<br>

**How to run "Tree_Paraphraser_app.py"**<br>
In order to run the script "Tree_Paraphraser_app.py" you need to install "TreeParaphraser.py" and "Tree_Paraphraser_app.py" in the same directory. You also need to install the flask framework and the nltk library."  Then open a terminal or command prompt and navigate to the directory where the file is saved. Then, run the command python "Tree_Paraphraser_app.py" to start the Flask server.  Once the server is running, you can open a web browser and navigate to "http://localhost:8080/paraphrase" and pass in the tree parameter with the сonstituency-based parse tree as a string and the maximum number of paraphrase trees parameter. Specify the port number as **8080**.

<br>

**For example:**<br><br>
http://localhost:8080/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter)%20)%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20G%C3%B2tic)%20)%20)%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets)%20)%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars)%20)%20(,%20,)%20(NP%20(NNS%20clubs)%20)%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants)%20)%20)%20)%20)%20)%20)%20)&limit=10  
<br>


**Execution result:**<br><br>

![result](https://user-images.githubusercontent.com/47922202/235253732-40ba0a44-87df-47ef-a23f-2669c546740f.png)



