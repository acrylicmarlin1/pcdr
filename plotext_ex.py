import plotext 
from io import StringIO
from contextlib import redirect_stdout



# class plotter:


#     """
#     >>> import numpy as np
#     >>> x = list(range(50))
#     >>> print(plotter.clean_plot(x, np.sin(x)))
#          ┌─────────────────────────────────┐
#      1.00┤▗▟  ▗▟   ▞▖  ▞▖  ▄▌  ▗▌  ▗▚   ▟  │
#      0.33┤▌▝▖ ▌ ▌ ▞ ▌ ▐ ▌ ▐ ▚ ▗▘▐ ▗▘▐  ▞▝▖ │
#     -0.33┤  ▌▗▘ ▚ ▌ ▚ ▌ ▝▖▞ ▐ ▐ ▝▖▐  ▌▐  ▚ │
#     -1.00┤  ▝▟   ▜   ▚▘  ▝▌  ▚▌  ▝▞  ▝▞   ▚│
#          └┬───────┬───────┬───────┬───────┬┘
#          0.0    12.2    24.5    36.8   49.0 
#     >>> print(plotter.clean_plot(x, np.sin(x), xsize=len(x), ysize=20))
#          ┌───────────────────────────────────────────┐
#      1.00┤ ▗    ▗▌   ▗▌    ▗     ▗    ▟     ▖        │
#          │ █    ▐▌   ▐▚    ▛▖   ▗▜    █    ▐▌   ▗▀▌  │
#          │▐▐    ▌▚   ▐▐    ▌▌   ▞▐    ▌▌   ▐▐   ▐ ▌  │
#      0.67┤▐▐   ▗▘▐   ▐ ▌   ▌▌   ▌▝▖   ▌▌   ▞▐   ▐ ▌  │
#          │▐ ▌  ▐ ▐   ▐ ▌  ▐ ▌   ▌ ▌  ▐ ▐   ▌▐   ▐ ▐  │
#      0.33┤▌ ▌  ▐  ▌  ▞ ▌  ▐ ▐   ▌ ▌  ▐ ▐   ▌▐   ▌ ▐  │
#          │▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐  ▐  ▐  ▐ ▐  ▗▘ ▌  ▌ ▐  │
#          │▌ ▐  ▌  ▌  ▌ ▐  ▞ ▐  ▐  ▐  ▐ ▐  ▐  ▌  ▌  ▌ │
#     -0.00┤▘ ▐  ▌  ▌  ▌ ▐  ▌ ▝▖ ▐  ▐  ▌  ▌ ▐  ▌ ▗▘  ▌ │
#          │  ▐  ▌  ▌ ▐  ▐  ▌  ▌ ▐  ▐  ▌  ▌ ▐  ▚ ▐   ▌ │
#          │  ▐  ▌  ▌ ▐  ▝▖ ▌  ▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐   ▌ │
#     -0.33┤   ▌▐   ▌ ▐   ▌▐   ▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐   ▌ │
#          │   ▌▐   ▚ ▐   ▌▐   ▐ ▌  ▐ ▐   ▐ ▌  ▐ ▐   ▌ │
#     -0.67┤   ▌▐   ▐ ▌   ▌▐   ▐ ▌  ▝▖▐   ▐ ▌   ▌▐   ▌ │
#          │   ▚▐   ▝▖▌   ▌▐   ▐ ▌   ▌▞   ▐▐    ▌▐   ▚ │
#          │   ▝▟    █    ▙▘    ▚▌   ▐▌   ▐▞    ▌▞   ▝▖│
#     -1.00┤    ▝    ▜    ▝          ▝▌   ▝▌    ▝     ▝│
#          └┬──────────┬─────────┬──────────┬─────────┬┘
#          0.0       12.2      24.5       36.8     49.0 
#     """
#     @classmethod
#     def clean_plot(self, xdata:list, ydata:list, xsize:int = 40, ysize: int = 7) -> str:
#         plotext.theme("clear")
#         plotext.plot_size(xsize, ysize)
#         plotext.plot(xdata, ydata)
#         with redirect_stdout(StringIO()) as stream:
#             plotext.show()
#         return stream.getvalue().replace("\x1b[0m", "")[:-1]


def docstring_plot(xdata: list, ydata: list, xsize: int = 40, ysize: int = 7):
    """
    >>> import numpy as np
    >>> x = list(range(50))
    >>> print(docstring_plot(x, np.sin(x)))
         ┌─────────────────────────────────┐
     1.00┤▗▟  ▗▟   ▞▖  ▞▖  ▄▌  ▗▌  ▗▚   ▟  │
     0.33┤▌▝▖ ▌ ▌ ▞ ▌ ▐ ▌ ▐ ▚ ▗▘▐ ▗▘▐  ▞▝▖ │
    -0.33┤  ▌▗▘ ▚ ▌ ▚ ▌ ▝▖▞ ▐ ▐ ▝▖▐  ▌▐  ▚ │
    -1.00┤  ▝▟   ▜   ▚▘  ▝▌  ▚▌  ▝▞  ▝▞   ▚│
         └┬───────┬───────┬───────┬───────┬┘
         0.0    12.2    24.5    36.8   49.0 
    >>> print(docstring_plot(x, np.sin(x), xsize=len(x), ysize=20))
         ┌───────────────────────────────────────────┐
     1.00┤ ▗    ▗▌   ▗▌    ▗     ▗    ▟     ▖        │
         │ █    ▐▌   ▐▚    ▛▖   ▗▜    █    ▐▌   ▗▀▌  │
         │▐▐    ▌▚   ▐▐    ▌▌   ▞▐    ▌▌   ▐▐   ▐ ▌  │
     0.67┤▐▐   ▗▘▐   ▐ ▌   ▌▌   ▌▝▖   ▌▌   ▞▐   ▐ ▌  │
         │▐ ▌  ▐ ▐   ▐ ▌  ▐ ▌   ▌ ▌  ▐ ▐   ▌▐   ▐ ▐  │
     0.33┤▌ ▌  ▐  ▌  ▞ ▌  ▐ ▐   ▌ ▌  ▐ ▐   ▌▐   ▌ ▐  │
         │▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐  ▐  ▐  ▐ ▐  ▗▘ ▌  ▌ ▐  │
         │▌ ▐  ▌  ▌  ▌ ▐  ▞ ▐  ▐  ▐  ▐ ▐  ▐  ▌  ▌  ▌ │
    -0.00┤▘ ▐  ▌  ▌  ▌ ▐  ▌ ▝▖ ▐  ▐  ▌  ▌ ▐  ▌ ▗▘  ▌ │
         │  ▐  ▌  ▌ ▐  ▐  ▌  ▌ ▐  ▐  ▌  ▌ ▐  ▚ ▐   ▌ │
         │  ▐  ▌  ▌ ▐  ▝▖ ▌  ▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐   ▌ │
    -0.33┤   ▌▐   ▌ ▐   ▌▐   ▌ ▌  ▐  ▌  ▌ ▌  ▐ ▐   ▌ │
         │   ▌▐   ▚ ▐   ▌▐   ▐ ▌  ▐ ▐   ▐ ▌  ▐ ▐   ▌ │
    -0.67┤   ▌▐   ▐ ▌   ▌▐   ▐ ▌  ▝▖▐   ▐ ▌   ▌▐   ▌ │
         │   ▚▐   ▝▖▌   ▌▐   ▐ ▌   ▌▞   ▐▐    ▌▐   ▚ │
         │   ▝▟    █    ▙▘    ▚▌   ▐▌   ▐▞    ▌▞   ▝▖│
    -1.00┤    ▝    ▜    ▝          ▝▌   ▝▌    ▝     ▝│
         └┬──────────┬─────────┬──────────┬─────────┬┘
         0.0       12.2      24.5       36.8     49.0 
    """
    plotext.theme("clear")
    plotext.plot_size(xsize, ysize)
    plotext.plot(xdata, ydata)
    with redirect_stdout(StringIO) as stream:
        plotext.show()
    return stream.getvalue().replace("\x1b[0m", "")[:-1]


# def addOne(x):
#     """
#     >>> addOne(5)
#     6
#     """
#     return x + 2

# print(addOne(5))


# plotext.theme("clear")
# plotext.plot_size(30, 7)
# x = list(range(50))
# plotext.plot(x, alias_for_np_sin(x))
# with redirect_stdout(StringIO()) as stream:
#     plotext.show()

# graph = stream.getvalue().replace("\x1b[0m", "")
# print(graph)

# def docstringshow():
#     with redirect_stdout(StringIO()) as stream:
#         plotext.show()
#     print(stream.getvalue().replace("\x1b[0m", "")[:-1])
    