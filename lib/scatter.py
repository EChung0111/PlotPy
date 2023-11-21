import numpy as np
import matplotlib.pyplot as plt
import os

class scatter:

    def grapher(datafile, outputfile, delimiter=None, title="", xlabel="", ylabel="", label=None,
                yscale=1, xrange=None, yrange=None, xticks=None, yticks=None,
                linewidth=None, color=None, yerr=None, xerr=None, mode='singlex'):
        
        with open(datafile, "r") as data_file:
            delim_str = delimiter if delimiter is not None else " "
            datalist = [line for line in data_file if delim_str in line]
            filelist = list(data_file)

        if datalist == filelist:
            data_array = np.genfromtxt(datafile, dtype=float, delimiter=delimiter)
            if mode == 'singlex':
                xlist = data_array[:, 0]

            

                ydata = np.delete(data_array, 0, 1)
                ydatadim = ydata.ndim
                
                fig, ax = plt.subplots(1, 1)

                for col in range(len(ydata[0, :])):
                    ylist = ydata[:, col] if ydatadim != 1 else ydata

                    label_current = label[col] if label and len(label) >= len(ydata[0, :]) else None
                    color_current = color[col] if color and len(color) >= len(ydata[0, :]) else None

                    if yerr is None and xerr is None:
                        ax.scatter(xlist, ylist, label=label_current, linewidth=linewidth, color=color_current)
                    elif yerr is not None and xerr is None:
                        ax.errorbar(xlist, ylist, label=label_current, linewidth=linewidth, ecolor=color_current, yerr=yerr)
                    elif xerr is not None and yerr is None:
                        ax.errorbar(xlist, ylist, label=label_current, linewidth=linewidth, ecolor=color_current, xerr=xerr)
                    else:
                        ax.errorbar(xlist, ylist, label=label_current, linewidth=linewidth, ecolor=color_current, yerr=yerr, xerr=xerr)

            else:
                row_len = len(data_array[0,:])
                if row_len%2 == 0:
                    xcol_del = row_len-1
                    xdata = data_array

                else:
                    print("Number of x coloums and y colums is not equal skipping last colum")
                    xdata = np.delete(data_array,row_len-1,1)
                
                while xcol_del > 0:
                    xdata =np.delete(xdata,xcol_del, 1)
                    xcol_del -= 2
            
            ax.set_ylabel(ylabel)
            ax.set_xlabel(xlabel)

            if isinstance(xrange, (list, np.ndarray)):
                ax.set_xlim(xrange[0], xrange[1])
            else:
                print("Invalid Type for X Range. X Range Must be list or array")

            if isinstance(yrange, (list, np.ndarray)):
                ax.set_ylim(yrange[0], yrange[1])
            else:
                print("Invalid Type for Y Range. Y Range Must be list or array")

            if isinstance(xticks, np.ndarray):
                ax.set_xticks(xticks)
            else:
                print("Invalid Type for X Ticks. X Ticks Must be an array")

            if isinstance(yticks, np.ndarray):
                ax.set_yticks(yticks)
            else:
                print("Invalid Type for Y Ticks. Y Ticks Must be an array")

            if label:
                ax.legend()

            ax.set_title(title)
            fig.tight_layout(pad=2)
            fig.savefig(os.path.join(outputfile),dpi=1000,bbox_inches="tight")
            plt.clf()
            plt.cla()
            
        else:
            print("ERROR: INVALID DELIMITER")
