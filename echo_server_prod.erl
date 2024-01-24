-module(echo_server_prod).
-export([start/0, loop/1]).

start() ->
    case gen_tcp:listen(12345, [binary, {packet, 0}, {active, false}, {reuseaddr, true}]) of
        {ok, ListenSocket} ->
            % spawn(fun() -> loop(ListenSocket) end);
            % io:format("Starting server ~n"),
            loop(ListenSocket);
        {error, Reason} ->
            io:format("Error starting server: ~p~n", [Reason])
    end.

loop(ListenSocket) ->
    case gen_tcp:accept(ListenSocket) of
        {ok, Socket} ->
            % spawn(fun() -> loop(ListenSocket) end),
            % io:format("Handling clients on ~p ~n", [Socket]),
            spawn(fun() -> handle_client(Socket) end),
            loop(ListenSocket);
            % handle_client(Socket);
        {error, Reason} ->
            io:format("Error accepting connection: ~p~n", [Reason])
    end.

handle_client(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            gen_tcp:send(Socket, Data),
            handle_client(Socket);
            % gen_tcp:close(Socket);
            % ok;
        {error, closed} ->
            % io:format("Closing Socket ~p~n", [Socket]),
            gen_tcp:close(Socket);
            % ok;
        {error, Reason} ->
            io:format("Error receiving data: ~p~n", [Reason])
    end.
