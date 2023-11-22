% -module(client).
% -export([start/0]).

% start() ->
%     {ok, Socket} = gen_tcp:connect("localhost", 12345, []),
%     Message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Sed at odio eu mauris malesuada facilisis. Fusce vitae hendrerit odio, nec efficitur ligula. In hac habitasse platea dictumst. Integer at mauris vel quam aliquam lacinia. Vestibulum tincidunt velit vel euismod varius. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin in sapien eu massa tincidunt mollis. Suspendisse nec velit quis velit condimentum fringilla. Nulla auctor vestibulum risus, non laoreet orci feugiat at. Quisque id tincidunt quam. Sed vehicula massa vel neque suscipit, ac fermentum lacus euismod. Suspendisse vitae libero auctor, feugiat mi nec, lacinia ex. Vivamus interdum fringilla tellus vel tincidunt. Donec nec consectetur purus, ac viverra mauris.",
%     io:format("Sending to server: ~s~n", [Message]),
%     gen_tcp:send(Socket, Message),
%     receive_response(Socket),
%     gen_tcp:close(Socket).

% receive_response(Socket) ->
%     receive
%         {tcp, Socket, Data} ->
%             io:format("Received from server: ~s~n", [Data])
%     end.

-module(client).
-export([start/0]).

start() ->
    {ok, Socket} = gen_tcp:connect("localhost", 12345, []),
    Message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Sed at odio eu mauris malesuada facilisis. Fusce vitae hendrerit odio, nec efficitur ligula. In hac habitasse platea dictumst. Integer at mauris vel quam aliquam lacinia. Vestibulum tincidunt velit vel euismod varius. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin in sapien eu massa tincidunt mollis. Suspendisse nec velit quis velit condimentum fringilla. Nulla auctor vestibulum risus, non laoreet orci feugiat at. Quisque id tincidunt quam. Sed vehicula massa vel neque suscipit, ac fermentum lacus euismod. Suspendisse vitae libero auctor, feugiat mi nec, lacinia ex. Vivamus interdum fringilla tellus vel tincidunt. Donec nec consectetur purus, ac viverra mauris.",
    io:format("Sending to server: ~s~n", [Message]),
    gen_tcp:send(Socket, Message),
    receive_response(Socket),
    gen_tcp:close(Socket).

receive_response(Socket) ->
    receive
        {tcp, Socket, Data} ->
            io:format("Received from server: ~s~n", [Data]);
            % receive_response(Socket);
        {tcp_closed, Socket} ->
            io:format("Connection closed by server~n")
    end.
