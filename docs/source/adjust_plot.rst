Changing the Plot View
----------------------

In the simulation plot frame, the following mouse actions by default will adjust the plot:

* **Left mouse click and drag**: moves the plot.
* **Right mouse click and drag**: compresses/stretches the plot
  (left/right horizontally, up/down vertically).
* **Middle scroll wheel**: zoom in/out.
* after an adjustment has been made,
  clicking the "A" symbol in the lower left corner resets the view.

In addition to these actions,
a single right mouse button-click will open a context menu
(this feature is built into the :code:`pyqtgraph` widget used to create the plots).
Many of these options aren't useful for NMR plots, but here are some options that are useful:

* **X Axis** and **Y Axis** let you select the x- and y- range for the plot.
  In addition to this,
  selecting the "Auto" radio button under **Y Axis** ensures that the largest peak uses the entire vertical range.
  This is very useful for DNMR simulations,
  because as line widths broaden towards coalescence their intensity is greatly reduced.
  Selecting this option allows the signal to fill the window, and scale the y-axis labels as needed.

* **Mouse Mode ▶ 1 button** changes the default mouse behavior,
  so that clicking and dragging a rectangular region of the spectrum zooms to that region.

* **Export...** allows you to save the plot in a variety of formats,
  including PNG, TIF, JPG and SVG.
  You can also export the plot data as a CSV file.