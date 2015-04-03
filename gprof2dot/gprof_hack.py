from gprof2dot import themes, formats, DotWriter
from StringIO import StringIO

def convert_to_dot(prof_string):
    """Main program."""

    output = StringIO()
    theme = themes['color']
    total_method = 'callratios'
    node_thresh = 0.5
    edge_thresh = 0.1

    # for Format in formats.values():
    # try: 
    # if Format.multipleInput:
    #     continue

    Format = formats['prof']

    parser = Format(StringIO(prof_string))
    profile = parser.parse()

    dot = DotWriter(output)
    dot.strip = True
    dot.wrap = True
    profile.prune(node_thresh / 100.0, edge_thresh / 100.0)

    dot.graph(profile, theme)

        # except Exception as e:
        #     print e
        #     continue
    
    return output.getvalue()
