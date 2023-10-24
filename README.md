## README

Hello!

We provide you with the script we use to visualize the entire Mandelbrot and Julia sets.

# Operation:

The command **MandelbrotPlot -o mandelbrot.png** displays the Mandelbrot set and saves it as an image named "mandelbrot."
The command **MandelbrotPlot --zmin=-0.7440+0.1305j --zmax=-0.7425+0.1320j --pixel_size=5e-6 --max-iter=50 -o Mandelbrot_tentacle.png** displays the complex numbers between zmin and zmax that belong to the Mandelbrot set and saves them in an image named Mandelbrot_tentacle.

The same commands are available for the Julia set. You can specify the c parameter if you wish (e.g., -c 0.251).

# Help:

The command **MandelbrotPlot -h** and the command **JuliaPlot -h** provide you with more information.

To avoid excessive waiting times, we recommend selecting an appropriate pixel size. For example:
 - A pixel size on the order of 5e-6 is suitable for displaying the Mandelbrot set.
 - A pixel size on the order of 5e-3 is suitable for displaying the Julia set.

The library uses numpy, Pillow, and unit tests can be conducted using Pytest.


# Documentation:
Documentation is readily accessible as I have created an automated one using Sphinx. To access it, follow these steps:

1. Navigate to the "doc" directory using the command:
   ```bash
   cd doc
   ```

2. Start a local web server to host the documentation using Python's `http.server` module:
   ```bash
   python -m http.server
   ```

3. Once the server is up and running, you can access the documentation by opening a web browser and entering the following address:
   ```
   http://localhost:8000/
   ```

This will allow you to explore the documentation locally on your machine. You'll find detailed information on how to use the software, its features, and other relevant information.
