-module(echo_clients).
-export([start/1, start_clients/2]).

start(Message) ->
    {ok, Socket} = gen_tcp:connect("localhost", 12345, [binary, {packet, 0}, {active, false}]),
    gen_tcp:send(Socket, Message),
    receive_response(Socket).

% start_clients(Message, NumClients) ->
%     lists:foreach(fun(_) ->
%         spawn(fun() -> start(Message) end)
%     end, lists:seq(1, NumClients)).

start_clients(_, 0) ->
    ok;
start_clients(Message, NumClients) ->
    spawn(fun() -> start(Message) end),
    start_clients(Message, NumClients - 1).

receive_response(Socket) ->
    case gen_tcp:recv(Socket, 0) of
        {ok, Data} ->
            io:format("Received: ~p~n", [Data]);
        {error, closed} ->
            io:format("Connection closed by server ~p~n",[error])
    end.
