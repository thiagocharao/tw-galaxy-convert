To run the tests

	python -m unittest discover tests -vv

To run with input file (The exercise input example)

	python main.py -i test_input.txt

To run

	python main.py

Reading and re-reading the challenges I fell in love with the Galaxy one. It was quite dificult for me to figure out a way to deal with roman numerals. But it worked and I loved it. I hope you like it too.

So, basically I divided the problem into contexts:

    units.py: I needed an abstraction for a way to quantitify Galaxy Unit. There is a TODO here, on to_roman method it
              would be possible to make that work using yield and a generator, although I spend a lot of time there
	          and that was not even the main goal. So it is a TODO now.

    resources.py: Also needed to find a way to keep track of resources of the system, here I wanted to create an
                  agnostic way to create new resources, it would be possible using a list of dicts. But I tended
		          to use a Factory because it would be nicer to have Strong instances of each resource. (at least that's my opinion)

    services.py: Also I wanted to keep business separated so, there is a Manager which is a bit more specialized,
                 knowing Resources and Units.

    interpreter.py: The way I found to be a gateway, receiving incoming messages and knowing what to do with those
                    messages and answering when there was a question.

    exceptions.py: Well, Exceptions...
                   Actually, there is something here, I wanted to specialize BusinessExceptions, so any Business Exception
		           raised, will have its message shown to the user.

    main.py: The program, some tricks to deal with arguments here, but nothing fancy. The only special point here is the
             talk_to_interpreter function, which decides when it can show a message and stay running.

    tests/*: The tests.
