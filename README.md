<div id="file-readme-template-md-readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0">
	    <article class="markdown-body entry-content container-lg" itemprop="text">
				<h1>
					<a id="user-content-project-title" class="anchor" aria-hidden="true" href="#project-title">
						<svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true">
							<path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z">
							</path>
						</svg>
					</a>Recobot</h1>
	<p>The aim of this project is to carry on object classification based on images published by "The occular engine" named "Archillect" on Twitter
	Each 30 minutes, Archillect's last tweet is taken and recoBot answers to him with the proboability of what he recognizes according to him<br/><br/>
	To do so, a Raspberry server is connected to twitter using Twitter API. Each 30 minutes, it takes last Arhillect's tweet and gives it to
	a neural network (deployed on the raspberry) using Tensorflow API (Tensorflow Lite).
</p>
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
		</p>
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

	
	</article>
  </div>
