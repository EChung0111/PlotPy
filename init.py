import numpy as np
import os
import sys
import fnmatch
import warnings
import lib.line as line
import lib.scatter as scatter

def getfiles(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file

arg_list = sys.argv

if "--help" not in arg_list or "--h" not in arg_list or "--version" not in arg_list or "--v" not in arg_list:

    if '--wd' in arg_list:
        working_dir = str(arg_list[arg_list.index('--wd')+1])
    else:
        working_dir = os.path.abspath('')
    
    if '--m' in arg_list:
        mode_str = str(arg_list[arg_list.index('--m')+1])
       
    else:
        mode_str = 'singlex'
    
    if '--g' in arg_list:
        graph_type = str(arg_list[arg_list.index('--g')+1])
    else:
        warnings.warn("No graph type specified")
        graph_type = None
    
    if '--i' in arg_list:
        input_file_str = str(arg_list[arg_list.index('--i')+1])
        if ',' in input_file_str:
            file_list = input_file_str.split(',')
        else:
            file_list = [input_file_str]
        
        for file in file_list:
            if '*' in file:
                filelist = [filestr for filestr in getfiles(working_dir) if fnmatch.fnmatch(filestr, file)]
                file_list = filelist

    else:
        warnings.warn("No input file(s) specified")
        file_list = None
    
    if '--o' in arg_list:
        output_file_str =str(arg_list[arg_list.index('--o')+1])

        if ',' in output_file_str:
            out_file_list = output_file_str.split(',')
        else:
            out_file_list = [output_file_str]
    
    else:
        out_file_list = []
        for file in file_list:
            file_name_list = file.split('.')
            file_name = file_name_list[0]
            out_file_list.append(f"{file_name}.png")

    if '--color' in arg_list:
        color_str = str(arg_list[arg_list.index('--color')+1])
        
        if ',' in color_str:
            color_list = color_str.split(',')
        else:
            color_list = [color_str]

    else:
        color_list = None

    if '--d' in arg_list:
        delimiter_str = str(arg_list[arg_list.index('--d')+1])
    else:
        delimiter_str = None
    
    if '--xlabel' in arg_list:
        xlabel_str = str(arg_list[arg_list.index('--xlabel')+1])
    else:
        xlabel_str = None

    if '--ylabel' in arg_list:
        ylabel_str = str(arg_list[arg_list.index('--ylabel')+1])
    else:
        ylabel_str = None

    if '--t' in arg_list:
        title_str = str(arg_list[arg_list.index('--t')+1])
    else:
        title_str = None
    
    if '--label' in arg_list:
        label_str = str(arg_list[arg_list.index('--label')+1])
        if '--' not in label_str:
            if ',' in label_str:
                label_list = label_str.split(',')
            else:
                warnings.warn("Need to delimit labels with commas")
    else:
        label_list = None
    
    if '--xrange' in arg_list:
        xrange_str = str(arg_list[arg_list.index('--xrange')+1])
        if ',' in xrange_str:
            xrange_list = xrange_str.split(',')
            xrange_list = np.array(xrange_list,dtype=float)
        else:
            warnings.warn("Need to specify 2 numbers for xrange (xmin,xmax)")
            xrange_list = None
    else:
        xrange_list = None
    
    if '--xticks' in arg_list:
        if xrange_list is not None:
            xticks = float(arg_list[arg_list.index('--xticks')+1])
            xtick_list = np.arange(xrange_list[0],xrange_list[1]+xticks,xticks)
        else:
            warnings.warn("No xrange specified")
    else:
        xtick_list = None
    
    if '--yrange' in arg_list:
        xrange_str = str(arg_list[arg_list.index('--yrange')+1])
        if ',' in xrange_str:
            yrange_list = xrange_str.split(',')
            yrange_list = np.array(xrange_list,dtype=float)
        else:
            warnings.warn("Need to specify 2 numbers for xrange (xmin,xmax)")
            yrange_list = None
    else:
        yrange_list = None
    
    if '--yticks' in arg_list:
        if xrange_list is not None:
            yticks = float(arg_list[arg_list.index('--yticks')+1])
            ytick_list = np.arange(yrange_list[0],yrange_list[1]+yticks,yticks)
        else:
            warnings.warn("No yrange specified")
    else:
        ytick_list = None
    
    if ("--linewidth" in sys.argv) and (graph_type == "line"):
        linewidth_index = sys.argv.index("--linewidth") +1
        linewidth = float(sys.argv[linewidth_index])
    else:
        linewidth = None
    
    if '--xerr' in arg_list:
        xerr = True
    else:
        xerr = False
    
    if '--yerr' in arg_list:
        yerr = True
    else:
        yerr = False

    for in_file,out_file in zip(file_list,out_file_list):
        if graph_type == 'line':

            in_file = os.path.join(working_dir,in_file)
            out_file = os.path.join(working_dir,out_file)

            line.line.grapher(datafile=in_file,outputfile=out_file,delimiter=delimiter_str,
                              title=title_str,xlabel=xlabel_str,ylabel=ylabel_str,
                              label=label_list,xrange=xrange_list,yrange=yrange_list,
                              xticks=xtick_list,yticks=ytick_list,linewidth=linewidth,
                              mode=mode_str,color=color_list)
        
        elif graph_type == 'scatter':
            scatter.scatter.grapher(datafile=in_file,outputfile=out_file,delimiter=delimiter_str,
                                    title=title_str,xlabel=xlabel_str,ylabel=ylabel_str,
                                    label=label_list,xrange=xrange_list,yrange=yrange_list,
                                    xticks=xtick_list,yticks=ytick_list,linewidth=linewidth,
                                    mode=mode_str,xerr=xerr,yerr=yerr)
            
        else:
            warnings.warn("Invalid graph type")

elif ('--help' in arg_list or '--h' in arg_list) and ('--v' not in arg_list or '--version' not in arg_list):
    help_message = """
    About This Program:
This is a command line based graphing software developed by Eugene Chung. This program can be usefull for data analysis of bulk data that needs to be graphed.
You can use --help or --h to see this page. Below you find some information regarding how to use the program and how to format your data.

    Input and Output:
    --i <input Filename>                             Input file with data to graph (.dat, .csv, etc. You may use unix command line arguments like * and ? to have multiple inputs)
    --o <Output Filename>                            Output file of graph (Default will have the same name as the inputfile) (.png, .jpg)
    --wd <Working Directory>                         Working Directory location of input and outfiles (Default is Current Directory)

    Graphing Options:
    --g <line>                                  Type of graph to be used       
    --title <Graph Title>                           Title for the graph (Default is No Title)
    --xlabel <X Axis Label>                         X axis label for the graph (Default is No Label)
    --ylabel <Y Axis Label>                         Y axis label for the graph (Default is No Label)
    --label <Label1,Label2,Label3,...,Labeln>       Label for the grph (Default is No Label)
    --xrange <xmin,xmax>                            Specify the range of the x axis (Default is automated range selection)
    --yrange <ymin,ymax>                            Specify the range of the y axis (Default is automated range selection)
    --xticks <X Increment>                          Specify the increment of the tickmarks on the x axis (Default is automated increment selection)
    --yticks <Y Increment>                          Specify the increment of the tickmarks on the y axis (Default is automated increment selection)
    --linewidth <float>                             Specifies line width for line graphs (Default is linedwidth=3)
    --color <color1,color2,...,colorn>              Specifies colors for graph

    Data Format Optioms:
    --d <delimiter option>                  Specify delimiter to seperate data entries in data file (Default is whiteshpace)
    --m <singlex or multix>                         Specify if you have one x column or multiple x columns (Default is singlex)

    Data Format Example
    This is an example of how you should format your data to graph it.

    Singlex
    X   Y1   Y2   Y3  ... Yn
    x1  y11  y21  y31 ... yn1
    x2  y12  y22  y32 ... yn2
    x3  y13  y23  y33 ... yn3
    .   .    .    .   ... .
    .   .    .    .   ... .
    .   .    .    .   ... .
    xm  y1m  y2m  y3m ... ynm

    Multix
    X1   Y1   X2   Y2   X3   Y3  ... Yn
    x11  y11  x21  y21  x31  y31 ... yn1
    x12  y12  x22  y22  x32  y32 ... yn2
    x13  y13  x23  y23  x33  y33 ... yn3
    .    .    .    .    .    .   ... .
    .    .    .    .    .    .   ... .
    .    .    .    .    .    .   ... .
    x1m  y1m  x2m  y2m  x3m  y3m ... ynm

    """
    print(help_message)

elif ("--help" not in arg_list or "--h" not in arg_list) and ("--version" in arg_list or "--v" in arg_list):
    version = '0.0.0'
    print(version)