-module(echo_client_prod).
-export([start/1, start_clients/2]).

start(Message) ->
    case gen_tcp:connect("localhost", 12345, [binary, {packet, 0}, {active, false}]) of
        {ok, Socket} ->
            gen_tcp:send(Socket, Message),
            receive_response(Socket),
            gen_tcp:close(Socket);
        {error, econnrefused} ->
            start(Message);
        {error, Reason} ->
            io:format("Error connecting to server: ~p~n", [Reason])
    end.

start_clients(_, 0) ->
    ok;
start_clients(Message, NumClients) when NumClients > 0 ->
    spawn(fun() -> start(Message) end),
    % start(Message),
    start_clients(Message, NumClients - 1).

receive_response(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            io:format("Received: ~p~n", [Data]);
        {error, closed} ->
            io:format("Connection closed by server ~p~n",[Socket]);
        {error, Reason} ->
            io:format("Error receiving data: ~p~n", [Reason])
    end.
