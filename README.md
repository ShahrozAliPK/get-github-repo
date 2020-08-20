<h1>Get-GitHub-Repo</h1>

<h2>What is Automation?</h2>
<h3>A little background</h3>
<p>Sometimes we just need to stop typing on the keyboard, hold a cup of coffee in hands,sit back and let the computer automate all the
    tasks on its own to get the most accurate search results so that we can quickly wind-up other things and move onto next task.
    At this point a term called <b>Automation</b> comes handy which takes the burden of all the recursive steps and produces the desired
    output without <i>human interference.</i></p>

<h3>But Why?</h3>
<p>Today, where hundreds of millions and billions of information and data are updated at every notch of a second and thousands of
    requests are made by millions of people regularly so it becomes super difiicult to manage,manipulate,search and update data of a
    particular search filter and qualifier.That's why <b><i>Automation</i></b> makes computer handle the recursive steps
    and keep querying the results until a break or base condition is met.Similarly in the world of Git and GitHub, automated scripts
    and programs can be super useful to manage and search repos and projects.</p>

<h2>Description</h2>
<p>Let's suppose you have to get all the contents of <i>hello-world</i> repository of <i>user: hellocat.</i>So basically there are two ways
    to approach this problem:</p>
    <ul>
      <li>First one is old traditional method of opening your browser first.Head to the URL address bar.Type <i>github.com/user_name.</i>
          Get to the homepage.Go to repositories.Then keep scrolling your mouse down until you find your desired repo and then click
          on it to open its content.</li>

   <br>

   <li>Second one is super fast and intelligent.You run my Python program.You just type <i>username</i> of a person and boom
          you are done, all the repositories of that <i>username</i> along with info and data are printed on your screen.Then you
          just type the correct <i>repo_no</i> to access and see all the contents of that repo along with <i>URL.</i>Well, pretty nice
            huh?</li>
    </ul>

<h2>How my program works?</h2>
<p>Well, its pretty nice and decent.You can open the <i>.py code</i> and read the comments so that you can understand on your own.
    The program uses <i>REST API</i> and <i>GitHub API</i> to access all the public ids and repositories so that you can access the
    contents.A simple <i>request</i> is made to get the repo data of <i>input: username</i> and then correct <i>repo_no</i> is used
    to pass <i>repo_name</i> to function which again make <i>request</i> and stores JSON response in the form of list.</p>
