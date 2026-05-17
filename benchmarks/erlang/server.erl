% -module(server).
% -export([start/0]).

% start() ->
%     {ok, ListenSocket} = gen_tcp:listen(12345, [{active, true}, {reuseaddr, true}]),
%     io:format("Server listening on port 12345~n"),
%     accept_clients(ListenSocket).

% accept_clients(ListenSocket) ->
%     {ok, Socket} = gen_tcp:accept(ListenSocket),
%     io:format("Accepted client connection: ~p~n", [Socket]),
%     loop(Socket),
%     accept_clients(ListenSocket).

% loop(Socket) ->
%     inet:setopts(Socket, [{active, once}]),
%     receive
%         {tcp, Socket, Data} ->
%             io:format("Received from client (~p): ~s~n", [Socket, Data]),
%             ReversedData = lists:reverse(Data),
%             io:format("Reversed message: ~s~n", [ReversedData]),
%             gen_tcp:send(Socket, ReversedData),
%             loop(Socket);
%         {tcp_closed, Socket} ->
%             io:format("Client (~p) disconnected~n", [Socket])
%     end.

-module(server).
-export([start/0, accept_clients/1, handle_client/1]).

start() ->
    {ok, ListenSocket} = gen_tcp:listen(12345, [{active, true}, {reuseaddr, true}]),
    io:format("Server listening on port 12345~n"),
    spawn(fun() -> accept_clients(ListenSocket) end).
    % accept_clients(ListenSocket).

accept_clients(ListenSocket) ->
    {ok, Socket} = gen_tcp:accept(ListenSocket),
    io:format("Accepted client connection: ~p~n", [Socket]),
    handle_client(Socket),
    % spawn(fun() -> handle_client(Socket) end),
    accept_clients(ListenSocket).

handle_client(Socket) ->
    inet:setopts(Socket, [{active, true}]),
    io:format("Handling client ~p~n", [Socket]),
    handle_client_loop(Socket).

handle_client_loop(Socket) ->
    receive
        {tcp, Socket, Data} ->
            io:format("Received from client (~p): ~s~n", [Socket, Data]),
            ReversedData = Data,
            % ReversedData = lists:reverse(Data),
            io:format("Reversed message: ~s~n", [ReversedData]),
            case gen_tcp:send(Socket, ReversedData) of
                ok ->
                    io:format("Sent response to client (~p): ~s~n", [Socket, ReversedData]);
                {error, Reason} ->
                    io:format("Error sending data to client (~p): ~p~n", [Socket, Reason])
            end,
            handle_client_loop(Socket);
        {tcp_closed, Socket} ->
            io:format("Client (~p) disconnected~n", [Socket]);
        OtherMessage ->
            % Handle other types of messages if necessary
            io:format("Received unexpected message: ~p~n", [OtherMessage]),
            handle_client_loop(Socket)
    end.




