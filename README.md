<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction-to-rag">Introduction to RAG</a></li>
    <li><a href="#environment-setup">Environment Setup</a></li>
    <li><a href="#run-the-code">Run the code</a></li>
  </ol>
</details>

<h2 id="introduction-to-rag">Introduction to RAG</h2>
<p>
Retrieval-Augmented Generation (RAG) is a technique/process which enhances the capabilities of large language models (LLMs), which access knowledge base outside of its training data before response. It can generate more accurate, up-to-date relevant responses, all without the need to retrain the model and best part is, its time and cost-efficient.<br/>

RAG's efficient approach includes Indexing, Vectorization, Chunking etc.<br/>

Lets see an example by Building an AI chatbot in Python that lets you chat with uploaded simple pdf file
</p>

<h2 id="environment-setup">Environment Setup</h2>
<ol>
  <li>
    Download / Clone code from<br/>
    https://github.com/eshwargirigowda/RAG_Chat_Application<br/>
    and open in your IDE, I am using VSCode<br/><br/>
  <li>
    Set virtual environment<br/>For windows systems, open Terminal and run the cmd (command) as shown below<br/>
    c:\>python -m venv venv<br/>
    c:\>venv\Scripts\activate<br/><br/>
  </li>
  <li>
    create/Update file</br>
    .env</br>
    with your openai api key<br/>
    OPENAI_API_KEY="your API Key"</br></br>
  </li>
  <li>
    Install all the requirement packages by running pip cmd</br>
    c:\>pip install -r .\requrements.txt</br></br>
  </li>
  <li>
    Make sure you have Docker Desktop installed and its running</br></br>
  </li>
  <li>
    Now run cmd as shown below</br>
    c:\>docker-compose up</br></br>
    Make sure file "docker-compose.yml" is at the prompt.</br>
    in above e.g. its c:\</br></br>
  </li>
</ol>

<h2 id="run-the-code">Run the code</h2>
 open Terminal and run the cmd (command) as shown below<br/>
 c:\>streamlit run main.py<br/><br/>

  You can now view your Streamlit app in your browser.<br/>

  Local URL: http://localhost:8501<br/>
  Network URL: http://192.168.2.102:8501<br/>

  Note:- IP and Port number will be displayed based on your system.<br/>
