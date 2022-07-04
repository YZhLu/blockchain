var beltDB;
var userAccount;

window.addEventListener('load', function () {

    web3Provider = null;
    // Browsers modernos já injetam web3 automaticamente.
    if (window.ethereum) {
        web3Provider = window.ethereum;
        try {
            window.ethereum.enable();
        } catch (error) {
            console.error("User denied account access")
        }
    }
    // Browsers antigos com MetaMask
    else if (window.web3) {
        web3Provider = window.web3.currentProvider;
    }
    // Se não detectar instância web3, conectar ao Ganache local.
    else {
        console.log('No web3? You should consider trying MetaMask!')
        web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
    }
    web3 = new Web3(web3Provider);
    startApp()



    function startApp() {
        var beltDBAddress = "0x29af3f6aaec1bfa45f4c172a91e4c047ef0465b5";//contract ADDRESS HERE!!!!
        beltDB = new web3.eth.contract(beltDBABI, beltDBAddress);
        /*
            var accountInterval = setInterval(function() {
            // Check if account has changed
                if (web3.eth.accounts[0] !== userAccount) {
                    userAccount = web3.eth.accounts[0];
                    // Call a function to update the UI with the new account
                    //getAthlete(userAccount)
                    //.then(displayAthlete);
                }
            }, 100);*/

        // Start here


        function displayAthlete(ids) {
            $("#athletes").empty();
            for (id of ids) {

                getAthleteDetails(id)
                    .then(function (athlete) {

                        $("#athletes").append(`<div class="athlete">
            <ul>
                <li>Id: ${athlete.id}</li>
                <li>Name: ${athlete.name}</li>
                <li>Birthday: ${athlete.birthdate}</li>
              </ul>
            </div>`);
                    });
            }
        }

        function addAthlete() {
            var _name = window.document.getElementById("txtName")
            var _birthdate = Date.parse(window.document.getElementById("bday"));
            var _firstTrainingDate = Date.parse(window.document.getElementById("tday"));
            // This is going to take a while, so update the UI to let the user know
            // the transaction has been sent
            $("#txStatus").text("Adding new athletes on the blockchain. This may take a while...");
            // Send the tx to our contract:
            return beltDB.methods.addAthlete(_name, _birthdate, _firstTrainingDate)
                .send({ from: userAccount })
                .on("receipt", function (receipt) {
                    $("#txStatus").text("Successfully added " + _name + "!");
                    // Transaction was accepted into the blockchain, let's redraw the UI
                    //getAthlete(userAccount).then(displayAthlete);
                })
                .on("error", function (error) {
                    // Do something to alert the user their transaction has failed
                    $("#txStatus").text(error);
                });
        }

        function promoteAthlete(_address) {
            $("#txStatus").text("Promoting an athlete. This may take a while...");
            return beltDB.methods.promoteAthlete(_address)
                .send({ from: userAccount })
                .on("receipt", function (receipt) {
                    $("#txStatus").text("Athlete promoted");
                    
                })
                .on("error", function (error) {
                    $("#txStatus").text(error);
                });
        }

        function editAthlete(_address, _belt) {
            $("#txStatus").text("Editing Athlete belt...");
            return beltDB.methods.editAthlete(_address, _belt)
                .send({ from: userAccount })
                .on("receipt", function (receipt) {
                    $("#txStatus").text("Athlete successfully leveled up");
                })
                .on("error", function (error) {
                    $("#txStatus").text(error);
                });
        }

        function getAthleteDetails(id) {
            return beltDB.methods.athletes(id).call()
        }

        function athleteToId(id) {
            return beltDB.methods.athleteToId(id).call()
        }

        function getAthlete(_address) {
            return beltDB.methods.getAthlete(_address).call()
        }

        window.addEventListener('load', function () {

            // Checking if Web3 has been injected by the browser (Mist/MetaMask)
            if (typeof web3 !== 'undefined') {
                // Use Mist/MetaMask's provider
                web3js = new Web3(web3.currentProvider);
            } else {
                // Handle the case where the user doesn't have Metamask installed
                // Probably show them a message prompting them to install Metamask
            }

            // Now you can start your app & access web3 freely:
            startApp()

        })


        //function getAthlete(){
        //var name = window.document.querySelector("input#athleteId")

        //name.innerHTML = `Name: ${hora}.`



        //}

    }

})