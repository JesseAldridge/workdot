import time, sys, os, subprocess, re

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Watcher(PatternMatchingEventHandler):
  def on_modified(self, event):
    print 'modified:', event.src_path
    if event.src_path.endswith('.txt'):
      dot_path = re.sub('.txt$', '.dot', event.src_path)
      subprocess.call(['python', 'to_graphviz.py', event.src_path, dot_path])
      subprocess.call(['open', dot_path])

dir_path = os.path.expanduser(sys.argv[1])

observer = Observer()
observer.schedule(Watcher(), path=dir_path)
observer.start()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()
  observer.join()
