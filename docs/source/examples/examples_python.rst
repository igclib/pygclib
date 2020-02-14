##################################
Python Examples
##################################


Build a race and save it to disk
=================================

::

    from pygclib.core.race import Race

    r =  Race(tracks='tracks/', task='task.xctsk')
    r.save('race.pkl')


Load a race and save it as json
===============================

::

    from pygclib.core.race import Race

    r =  Race(path='race.pkl')
    r.save('race.json')


Get a task optimization info and save it as json
=================================================

::

    from pygclib.core.task import Task

    t = Task('task.xctsk')
    t.save('optimized.json')


Get all available tasks from a provider on standard output
==========================================================

::

    from pygclib.crawlers.task_crawler import TaskCrawler

    crawler = TaskCrawler(provider='PWCA', year=2015)
    crawler.save('-')
