import numpy as np
import matplotlib.pyplot as plt
import os

class line:

    def grapher(datafile, outputfile, delimiter=None, title="", xlabel="", ylabel="", label=None,
                xrange=None, yrange=None, xticks=None, yticks=None,
                linewidth=None, color=None, mode='singlex'):
        
        fig, ax = plt.subplots(1, 1)

        datalist = []
        filelist = []
        
        line_number_list = []
        line_number = 1

        datafile_open = open(datafile)

        for line in datafile_open:
            if delimiter in line:
                datalist.append(line)
                line_number_list.append(line_number)
                line_number += 1
            filelist.append(line)

        if datalist == filelist:
            data_array = np.genfromtxt(datafile, dtype=float, delimiter=delimiter)
            if mode == 'singlex':
                xdata = data_array[:, 0]
                xlist = list(xdata)

                ydata = np.delete(data_array, 0, 1)
                ydatadim = ydata.ndim

                for col in range(len(ydata[0, :])):
                    ylist = ydata[:, col] if ydatadim != 1 else ydata

                    label_current = label[col] if label and len(label) >= len(ydata[0, :]) else None
                    
                    if len(color) != 1:
                        color_current = color[col] if color and len(color) >= len(ydata[0, :]) else None
                    else:
                        color_current = color[0]
                    
                    ax.plot(xlist, ylist, label=label_current, linewidth=linewidth, color=color_current)

            elif mode == 'multix':
                row_len = len(data_array[0,:])
                if row_len%2 == 0:
                    xcol_del = row_len-1
                    ycol_del = xcol_del-1
                    xdata = data_array
                    ydata = data_array
                else:
                    print("Number of x coloums and y colums is not equal skipping last colum")
                    xdata = np.delete(data_array,row_len-1,1)
                    ydata = np.delete(data_array,row_len-1,1)
                    xcol_del = row_len-2
                    ycol_del = xcol_del-1
                
                while xcol_del > 0:
                    xdata =np.delete(xdata,xcol_del, 1)
                    xcol_del -= 2
                
                while ycol_del >=0:
                    ydata = np.delete(ydata,ycol_del, 1)
                    ycol_del -= 2
                
                for col in range(len(xdata[0,:])):
                    xlist = xdata[:,col]
                    ylist = ydata[:,col]
                
                    label_current = label[col] if label and len(label) >= len(ydata[0, :]) else None
                    
                    if len(color) != 1:
                        color_current = color[col] if color and len(color) >= len(ydata[0, :]) else None
                    else:
                        color_current = color[0]
                    
                    ax.plot(xlist, ylist, label=label_current, linewidth=linewidth, color=color_current)

            ax.set_ylabel(ylabel)
            ax.set_xlabel(xlabel)

            if xrange is not None:
                if isinstance(xrange, (list, np.ndarray)):
                    ax.set_xlim(xrange[0], xrange[1])
                else:
                    print("Invalid Type for X Range. X Range Must be list or array")

            if yrange is not None:
                if isinstance(yrange, (list, np.ndarray)):
                    ax.set_ylim(yrange[0], yrange[1])
                else:
                    print("Invalid Type for Y Range. Y Range Must be list or array")

            if xticks is not None:
                if isinstance(xticks, np.ndarray):
                    ax.set_xticks(xticks)
                else:
                    print("Invalid Type for X Ticks. X Ticks Must be an array")

            if yticks is not None:
                if isinstance(yticks, np.ndarray):
                    ax.set_yticks(yticks)
                else:
                    print("Invalid Type for Y Ticks. Y Ticks Must be an array")

            if label is not None:
                ax.legend(label,loc='best',fontsize=5)

            ax.set_title(title)
            fig.tight_layout(pad=2)
            fig.savefig(os.path.join(outputfile), dpi=1000, bbox_inches="tight")
            plt.clf()
            plt.cla()

        else:
            print("ERROR: INVALID DELIMITER")

            complete_line_number_list = range(1,len(filelist))
            for line_number in line_number_list:
                if line_number not in complete_line_number_list:
                    print(f"There is an issue at line: {line_number}")
