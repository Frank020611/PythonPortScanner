# Python TCP Port Scanner

## Project Description

I decided to build this project because I wanted to challenge myself with something more difficult and improve my problem-solving skills as a beginner in Python.

The program is a multithreaded TCP port scanner that allows users to scan a range of ports on a specified IPv4 address to check whether they are open or closed. It also includes input validation, configurable connection timeouts, automatic retries when connections time out, and multiple worker threads to scan ports concurrently.

## Features

- IPv4 address validation
- Custom starting and ending ports
- Configurable connection timeout
- Multithreaded scanning using `ThreadPoolExecutor`
- Configurable number of workers
- Automatic retry with a separate timeout when a connection times out
- Error handling for invalid inputs and connection failures
- Total scan execution time

## Requirements

- Python 3
- No external Python packages required

## How to Run

1. Download the project files.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

4. Enter the target IPv4 address, port range, timeout settings, and number of workers.
5. Review the scan results in the terminal.

## Local Testing

The project includes `test_server.py`, a simple local TCP server for testing port detection.

Run it in a separate terminal:

```bash
python test_server.py
```

Then run the scanner and test `127.0.0.1` on port `8080`.

The test server accepts one connection and then stops, so restart it before another test.

## What I Learned

While developing this project, I learned how to use Python functions and parameters, exception handling with `try/except` to handle invalid inputs and prevent unexpected crashes, TCP socket programming, and concurrent programming using worker threads.

I also learned how to validate user inputs, debug network connections, configure connection timeouts, and measure the total execution time of a program using `time.perf_counter()`.

Overall, I really enjoyed working on this project. It helped me improve my problem-solving skills significantly, especially when it came to understanding and handling a program that was quite complex for a beginner like myself.

## Future Improvements

- Ask users whether to retry timed-out ports after the initial scan
- Display a summary of scan results
- Improve the terminal output and result ordering

## Disclaimer

This project is intended for educational purposes and authorised network testing only. Only scan systems you own or have explicit permission to assess.