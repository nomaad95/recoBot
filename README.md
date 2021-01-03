<div id="file-readme-template-md-readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0">
	    <article class="markdown-body entry-content container-lg" itemprop="text">
				<h1>
					<a id="user-content-project-title" class="anchor" aria-hidden="true" href="#project-title">
						<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
							<path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z">
							</path>
						</svg>
					</a>Recobot</h1>

	<!--<p>The aim of this project is to carry on object classification based on images published by "The occular engine" named "Archillect" on Twitter
	Each 30 minutes, Archillect's last tweet is taken and recoBot answers to him with the proboability of what he recognizes according to him
	To do so, a Raspberry server is connected to twitter using Twitter API. Each 30 minutes, it takes last Arhillect's tweet and gives it to
	a neural network (deployed on the raspberry) using Tensorflow API (Tensorflow Lite).
</p> -->
	<h2>
		<a id="user-content-getting-started" class="anchor" aria-hidden="true" href="#getting-started">
			<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
				<path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z">
				</path>
			</svg>
		</a>Getting Started</h2>
	<p>
		-A PC (qui l'eut cru) running on Linux <br/><br/>
		-A Python3 interpreter<br/><br/>
		-Pip3 as Python package manager
		</p>	<!--
	<h3>
		<a id="user-content-prerequisites" class="anchor" aria-hidden="true" href="#prerequisites">
			<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
				<path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z">
				</path>
			</svg>
		</a>Prerequisites</h3>
	<p>In order to work recoBot needs some dependencies:<br/><br/>
	-Requests<br/><br/>
	-tweepty<br/><br/>
	-Tensorflow<br/></p>

	<h3>
	<a id="user-content-installing" class="anchor" aria-hidden="true" href="#installing">
		<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
			<path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z">
			</path>
		</svg>
	</a>Installing</h3>

	<p>How to install those ?
	<p>The following instructions will install the dependencies required</p>
	<pre><code>pip install requests
	</code></pre>
	<pre><code>pip install tweepy
	</code></pre>
	<pre><code>pip install tensorflow
	</code></pre></p>






	<h3><a id="user-content-installing" class="anchor" aria-hidden="true" href="#installing"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>About Tweepy</h3>
	<p>Tweepy is an API wich uses provides Twitter social network datas. <br/></p>
		<a>In order to use this API follow the steps to create a developer twitter account right <a href="https://realpython.com/twitter-bot-python-tweepy/#using-tweepyl">here</a>
		</a>




	<h2><a id="user-content-deployment" class="anchor" aria-hidden="true" href="#deployment"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Deployment</h2>
	<p>CAUTION</p>
		<a> The file bot.py imports another file called "apikey.py".<br/><br/>
		<a> Those keys are the ones Twitter gave to you when you created your.<br/><br/>
		<a>Twitter developer account. Hence, in order to make that project work you will have to <br/><br/>
		<a>fill the list returned by key() with yours <br/><br/>
	<p>Then run the following command line</p>
	<pre><code>python3 bot.py
	</code></pre>

	<a>Now you can have informations of what archillect is posting in real time <br/><br/>
	 <!-
	<ul>
	<li><a href="http://www.dropwizard.io/1.0.2/docs/" rel="nofollow">Dropwizard</a> - The web framework used</li>
	<li><a href="https://maven.apache.org/" rel="nofollow">Maven</a> - Dependency Management</li>
	<li><a href="https://rometools.github.io/rome/" rel="nofollow">ROME</a> - Used to generate RSS Feeds</li>
</ul>

	<h2><a id="user-content-authors" class="anchor" aria-hidden="true" href="#authors"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Author</h2>
	<ul>
	<li><strong>Camille Bamboute</strong> - <em>Junior software enginner</em></li>
	</ul>

	<h2><a id="user-content-acknowledgments" class="anchor" aria-hidden="true" href="#acknowledgments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tips</h2>
	<ul>
	<li>Dogecoin jar: D9JFfxeDesPfjjBCc7rh1eeS83n72o6Foq </li>
	</ul> -->
	</article>
  </div>
