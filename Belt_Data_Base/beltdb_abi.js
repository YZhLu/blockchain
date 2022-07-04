beltDBABI = [
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "athleteToId",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_athleteId",
				"type": "uint256"
			}
		],
		"name": "getAthleteById",
		"outputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "birthdate",
				"type": "uint256"
			},
			{
				"name": "firstTrainingDate",
				"type": "uint256"
			},
			{
				"name": "belt",
				"type": "uint8"
			},
			{
				"name": "promotionsDate",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_athleteAddress",
				"type": "address"
			},
			{
				"name": "_belt",
				"type": "uint8"
			}
		],
		"name": "editAthete",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"name": "addressToAthletes",
		"outputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "birthdate",
				"type": "uint256"
			},
			{
				"name": "firstTrainingDate",
				"type": "uint256"
			},
			{
				"name": "belt",
				"type": "uint8"
			},
			{
				"name": "id",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_athleteAddress",
				"type": "address"
			}
		],
		"name": "promoteAthlete",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_birthdate",
				"type": "uint256"
			},
			{
				"name": "_firstTrainingDate",
				"type": "uint256"
			}
		],
		"name": "addAthlete",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_athleteAdress",
				"type": "address"
			}
		],
		"name": "getAthlete",
		"outputs": [
			{
				"name": "id",
				"type": "uint256"
			},
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "birthdate",
				"type": "uint256"
			},
			{
				"name": "firstTrainingDate",
				"type": "uint256"
			},
			{
				"name": "belt",
				"type": "uint8"
			},
			{
				"name": "promotionsDate",
				"type": "uint256[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "addressToPromotionsDate",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "athletes",
		"outputs": [
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "birthdate",
				"type": "uint256"
			},
			{
				"name": "firstTrainingDate",
				"type": "uint256"
			},
			{
				"name": "belt",
				"type": "uint8"
			},
			{
				"name": "id",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "birthdate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "firstTrainingDate",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "belt",
				"type": "uint8"
			},
			{
				"indexed": false,
				"name": "promotionsDate",
				"type": "uint256[]"
			}
		],
		"name": "NewAthlete",
		"type": "event"
	}
]