
import plotext._utility


def clean_plot(xdata:list, ydata:list, xsize:int = 40, ysize: int = 7) -> str:   
    """
    >>> import numpy as np
    >>> x = list(range(50))
    >>> print(clean_plot(x, np.sin(x)))
         ┌─────────────────────────────────┐
     1.00┤▗▟  ▗▟   ▞▖  ▞▖  ▄▌  ▗▌  ▗▚   ▟  │
     0.33┤▌▝▖ ▌ ▌ ▞ ▌ ▐ ▌ ▐ ▚ ▗▘▐ ▗▘▐  ▞▝▖ │
    -0.33┤  ▌▗▘ ▚ ▌ ▚ ▌ ▝▖▞ ▐ ▐ ▝▖▐  ▌▐  ▚ │
    -1.00┤  ▝▟   ▜   ▚▘  ▝▌  ▚▌  ▝▞  ▝▞   ▚│
         └┬───────┬───────┬───────┬───────┬┘
         0.0    12.2    24.5    36.8   49.0 
    >>> print(clean_plot(x, np.sin(x), xsize=len(x), ysize=20))
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
    import plotext
    from contextlib import redirect_stdout
    from io import StringIO

    
    plotext.theme("clear")
    plotext.plot_size(xsize, ysize)
    plotext.plot(xdata, ydata)
    with redirect_stdout(StringIO()) as stream:
        plotext.show()
    plotext.clear_data()
    return stream.getvalue().replace("\x1b[0m", "")[:-1]
