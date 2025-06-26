from app.llm.azure import ask_azure_openai
from app.utils.utils import collect_code_files

full_code = collect_code_files(repo_path="/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/example/fastapi-sample")
log = """
    INFO:     Will watch for changes in these directories: ['/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/example/fastapi-sample']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [35813] using StatReload
    INFO:     Started server process [35822]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     127.0.0.1:49328 - "GET / HTTP/1.1" 404 Not Found
    INFO:     127.0.0.1:49328 - "GET /favicon.ico HTTP/1.1" 404 Not Found
    INFO:     127.0.0.1:49357 - "GET /docs HTTP/1.1" 200 OK
    INFO:     127.0.0.1:49357 - "GET /openapi.json HTTP/1.1" 200 OK
    WARNING:  StatReload detected changes in 'app/routes/hello.py'. Reloading...
    INFO:     Shutting down
    INFO:     Waiting for application shutdown.
    INFO:     Application shutdown complete.
    INFO:     Finished server process [35822]
    INFO:     Started server process [36541]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ^CINFO:     Shutting down
    INFO:     Waiting for application shutdown.
    INFO:     Application shutdown complete.
    INFO:     Finished server process [36541]
    INFO:     Stopping reloader process [35813]
    (venv) doli@EXT-CK9T32J3V3 fastapi-sample % python run.py
    INFO:     Will watch for changes in these directories: ['/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/example/fastapi-sample']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [36678] using StatReload
    INFO:     Started server process [36680]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     127.0.0.1:49512 - "GET /hello?name=World HTTP/1.1" 500 Internal Server Error
    ERROR:    Exception in ASGI application
    Traceback (most recent call last):
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/uvicorn/protocols/http/h11_impl.py", line 403, in run_asgi
        result = await app(  # type: ignore[func-returns-value]
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
        return await self.app(scope, receive, send)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__
        await super().__call__(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/applications.py", line 112, in __call__
        await self.middleware_stack(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/middleware/errors.py", line 187, in __call__
        raise exc
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/middleware/errors.py", line 165, in __call__
        await self.app(scope, receive, _send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 62, in __call__
        await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
        raise exc
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
        await app(scope, receive, sender)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/routing.py", line 714, in __call__
        await self.middleware_stack(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/routing.py", line 734, in app
        await route.handle(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/routing.py", line 288, in handle
        await self.app(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/routing.py", line 76, in app
        await wrap_app_handling_exceptions(app, request)(scope, receive, send)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
        raise exc
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
        await app(scope, receive, sender)
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/starlette/routing.py", line 73, in app
        response = await f(request)
                ^^^^^^^^^^^^^^^^
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/fastapi/routing.py", line 301, in app
        raw_response = await run_endpoint_function(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/venv/lib/python3.11/site-packages/fastapi/routing.py", line 212, in run_endpoint_function
        return await dependant.call(**values)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/doli/Projects/chendong-li/Automate-Software-QA-Testing-in-LLM/example/fastapi-sample/app/routes/hello.py", line 9, in say_hello
        result = 1 / 0
                ~~^~~
    ZeroDivisionError: division by zero
"""

response = ask_azure_openai(
    full_code=full_code,
    log=log
)

print("Response from LLM:", response)