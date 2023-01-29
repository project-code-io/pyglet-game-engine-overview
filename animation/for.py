while True:
    start = now()
    delta = last_tick - start

    for x in entities:
        x.update(delta)

    batch.draw()
    handle_input()

    sleep(1/60 - (now() - start))
    last_tick = now()
