# pyodide-pygame-demo

This is a simple demo project showing how you can export a [pygame-ce](https://pyga.me/) project to
the web using [Pyodide](https://pyodide.org/en/stable/). It displays a ball that changes colours and
bounces around the screen, inspired by the DVD logo. It was written as a demonstration for
[this article I wrote about Pygame on the web](https://www.sebastienfulmer.com/thoughts/pygame-on-the-web-with-pyodide/)
which details how it works and how to adapt your own project.

It uses [uv](https://docs.astral.sh/uv/) as the project manager and build system for the Python
code, and a simple `index.html` file to display it.

For this to work, you first need to build the project using `uv build` in order to produce the wheel
for the demo. Then, you need to start a HTTP server, for instance using `python3 -m http.server` or
`npx http-server`.

This uses pygame-ce rather than the original pygame as that is what Pyodide 0.29.0 comes bundled
with (see [Packages built in Pyodide](https://pyodide.org/en/0.29.0/usage/packages-in-pyodide.html)).

For a pygame-ce project to work with Pyodide, it needs to use `asyncio` so that control can be
returned to the browser (see
[Using SDL-based packages in Pyodide](https://pyodide.org/en/0.29.0/usage/sdl.html)). I
intentionally implemented the demo initially with `pygame.time.Clock` and then later moved it to
`asyncio` so that you can see the difference in the commit diffs
([5d9f7c1](https://github.com/CreatedBySeb/pyodide-pygame-demo/commit/5d9f7c144a0247a829ea531180354dc104587f36)).
Based on testing, even though `asyncio.sleep` should yield with a value of `0` according to the
[Python docs](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep), this does not seem
to work with Pyodide and so I opted to delay for 1/120th of a second instead. This is something you
may want to tune or find an alternative to yourself depending on the nature of your project.

This project is shared under the MIT License, see `LICENSE` for details.
