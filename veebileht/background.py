from background_task import background


@background(schedule=5)
def run_scheduled():
    print('hello console')
