
import numpy as np
import matplotlib.pyplot as plt

class reaction_coord:

    def grapher(datafile, outputfile, delimiter=None, title="", xlabel="", ylabel="", label=None,
                xrange=None, yrange=None, xticks=None, yticks=None,
                linewidth=1.5, color=None, mode='singlex', plat_len=None):

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
                ydata = data_array[:, 0]

                new_ydata = []
                for y_val in ydata:
                    if plat_len is not None:
                        for plat in range(plat_len):
                            new_ydata.append(y_val)
                            new_ydata.append(y_val)
                            new_ydata.append(y_val)

                ydata = new_ydata
                xlist = range(len(ydata))
                ydatadim = 1

                for col in range(len(ydata[0, :])):
                    ylist = ydata[:, col] if ydatadim != 1 else ydata

                    label_current = label[col] if label and len(label) >= len(ydata[0, :]) else None

                    if len(color) != 1:
                        color_current = color[col] if color and len(color) >= len(ydata[0, :]) else None
                    else:
                        color_current = color[0]

                    ax.plot(xlist, ylist, label=label_current, linewidth=linewidth, color=color_current, linestyle='dashed')

                    x_val = 0

                    no_rep_ylist = []
                    for val in ylist:
                        if val not in no_rep_ylist:
                            no_rep_ylist.append(val)

                    for yval in no_rep_ylist:

                        y_plat = []
                        x_plat = []

                        for plat_val in range(plat_len):
                            y_plat.append(yval)
                            x_plat.append(x_val)
                            x_val += 1

                        ax.plot(x_plat, y_plat, linewidth=linewidth*2.5, color=color_current, label='_nolegend_')

                    ax.set_xticks([])

            elif mode == 'multix':
                row_len = len(data_array[0, :])

                for col in range(row_len):
                    ylist = data_array[:, col]
                    new_ylist = []
                    for y_val in ylist:
                        if plat_len is not None:
                            for plat in range(plat_len):
                                new_ylist.append(y_val)

                    xlist = range(len(new_ylist))
                    ylist = new_ylist

                    label_current = label[col] if label and len(label) >= row_len else None

                    if len(color) != 1:
                        color_current = color[col] if color and len(color) >= row_len else None
                    else:
                        color_current = color[0]

                    ax.plot(xlist, ylist, label=label_current, linewidth=linewidth, color=color_current, linestyle='dashed')

                    x_val = 0

                    no_rep_ylist = []
                    for val in ylist:
                        if val not in no_rep_ylist:
                            no_rep_ylist.append(val)

                    for yval in no_rep_ylist:

                        y_plat = []
                        x_plat = []

                        for plat_val in range(plat_len):
                            y_plat.append(yval)
                            x_plat.append(x_val)
                            x_val += 1

                        ax.plot(x_plat, y_plat, linewidth=linewidth * 2.5, color=color_current, label='_nolegend_')

                    ax.set_xticks([])

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
                ax.legend(label, loc='best', fontsize=5)

            ax.set_title(title)
            fig.tight_layout(pad=2)

            return fig, ax

        else:
            print("ERROR: INVALID DELIMITER")

            complete_line_number_list = range(1, len(filelist))
            for line_number in line_number_list:
                if line_number not in complete_line_number_list:
                    print(f"There is an issue at line: {line_number}")
