import r2pipe, sys

def createR2Pipe():
    try:
        pipe = r2pipe.open()
        pipe.cmd('a')
        return pipe
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return None
