-module(echo_server).
-export([start/0, loop/1]).

start() ->
    {ok, ListenSocket} = gen_tcp:listen(12345, [binary, {packet, 0}, {active, false}, {reuseaddr, true}]),
    spawn(fun() -> loop(ListenSocket) end).

loop(ListenSocket) ->
    {ok, Socket} = gen_tcp:accept(ListenSocket),
    io:format("Handling client on ~p ~n", [Socket]),
    % spawn(fun() -> loop(ListenSocket) end),
    spawn(fun() -> handle_client(Socket) end),
    loop(ListenSocket).

handle_client(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            gen_tcp:send(Socket, Data),
            handle_client(Socket);
        {error, closed} ->
            ok
    end.
