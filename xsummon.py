#!/usr/bin/python3
import subprocess
import argparse


def run(command):
    # Parses a string, runs as bash command, returns output (or throws exception if something went wrong)
    response = subprocess.run(
        command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if response.returncode <= 1:
        return response.stdout.decode('utf-8')
    else:
        print(f'Returncode:{response.returncode}\n',
              response.stdout.decode('utf-8'))
        raise Exception


argparser = argparse.ArgumentParser(description='Call/hide a specific window.')
argparser.add_argument('program',
                       help='name of program')
argparser.add_argument('-a', '--args', default='',
                       help='passed to program if run by xsummon, example: xsummon firefox --args="--fullscreen" ')
argparser.add_argument('-g', '--go', action='store_true',
                       help="go to window's desktop instead of summoning it to the active desktop")
args = argparser.parse_args()

candidatePIDs = run(f'pgrep {args.program}').split()
windowInfos = [line.split()[:3] for line in run('wmctrl -lp').split('\n') if line]  # windowid, desktop, pid
print(f'Candidate PIDs for window process of {args.program}:\n', '\n'.join(candidatePIDs))

for windowID, windowDesktop, windowPID in windowInfos:
    if windowPID not in candidatePIDs:
        continue

    print('PID match found:', windowPID, '\nwindowID:', windowID)

    windowID = int(windowID, 16)
    windowDesktop = int(windowDesktop)

    activeWindowID = run('xdotool getactivewindow')
    if activeWindowID:
        activeWindowID = int(activeWindowID)

    activeDesktop = int(run('xdotool get_desktop'))

    # main logic
    if activeDesktop == windowDesktop:
        if activeWindowID == windowID:
            run(f'xdotool windowminimize {windowID}')
        else:
            run(f'xdotool windowactivate {windowID}')
    else:
        if args.go:
            run(f'xdotool set_desktop {windowDesktop}')
        else:
            run(f'xdotool set_desktop_for_window {windowID} {activeDesktop}')
        run(f'xdotool windowactivate {windowID}')
    break
else:
    run(' '.join([args.program, args.args]))
