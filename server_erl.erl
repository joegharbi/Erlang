-module(server_erl).
-export([start/0, loop/1]).

start() ->
    case gen_tcp:listen(12345, [binary, {packet, 0}, {active, false}, {reuseaddr, true}]) of
        {ok, ListenSocket} ->
            spawn(fun() -> loop(ListenSocket) end);
        {error, _} ->
            ok
    end.

loop(ListenSocket) ->
    case gen_tcp:accept(ListenSocket) of
        {ok, Socket} ->
            spawn(fun() -> handle_client(Socket) end),
            loop(ListenSocket);
        {error, _} ->
            ok
    end.

handle_client(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            gen_tcp:send(Socket, Data),
            handle_client(Socket);
        {error, closed} ->
            gen_tcp:close(Socket);
            % ok;
        {error, _} ->
            ok
    end.
