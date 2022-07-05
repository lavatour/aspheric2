import drawSvg as draw

d = draw.Drawing(200, 200, origin='center', displayInline=False)



# Draw an irregular polygon
d.append(draw.Lines(-80, -45, 70, -49,
                    95, 49,
                    -90, 40,
                    60, 40,
                    -100, 100, 0, 0,
                    close=False,
            stroke='black', stroke_width = .5,
            fill = 'none'))


d.setPixelScale(40)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')
d.savePng('example.png')

# Display in Jupyter notebook
d.rasterize()  # Display as PNG
d  # Display as SVG

