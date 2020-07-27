pragma solidity ^0.6.10;

contract sendmoney{
    
    uint256 public contractbalance;
    
    function receieveMoney()public payable{
        contractbalance+=msg.value;
    }
    
    /* Getting the balance of smart contract through function using this keyword*/
    
    function getBalance()public view returns(uint256){
        return address(this).balance;
    }
    //function to withdraw all the money from smart contact and send it to a 'to' address
    
    function withdraw()public{
        address payable to=msg.sender;
        contractbalance-=this.getBalance();
        to.transfer(this.getBalance());
        
    }
    
    // send contract balance to a given address and to only the one who call the transaction i.e., sender
    function sendtoaccount(address payable _to)public{
        _to.transfer(this.getBalance());
    }
}
