-module(echo_client).
-export([start/1]).

start(Message) ->
    {ok, Socket} = gen_tcp:connect("localhost", 12345, [binary, {packet, 0}, {active, false}]),
    gen_tcp:send(Socket, Message),
    receive_response(Socket).

receive_response(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            io:format("Received: ~p~n", [Data]);
        {error, closed} ->
            io:format("Connection closed by server~n")
    end.
