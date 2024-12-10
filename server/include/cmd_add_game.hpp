#ifndef __CMDADDGAME__
#define __CMDADDGAME__

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <mutex>
#include <algorithm>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <unordered_map>
#include <memory>
#include <sstream>

#include "abstract_command.hpp"
#include "server_controller.hpp"
#include "game.hpp"

class CmdAddGame : public AbstractCommand {
public:
    CmdAddGame(ServerController& controller) : controller(controller) {}

    void execute(const std::vector<int>& args, int client_number) {
        if (args.size() != 1) {
            std::cerr << "Error: must set number of players" << std::endl;
            return;
        }

        Game game(args[0], client_number);
        controller.add_game(client_number, game);
        controller.update_player_status(client_number, client_number);

        controller.send_call("Added game\n", client_number);
    }

private:
    ServerController& controller;
};

#endif // __CMDADDGAME__
