using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
namespace Arkademy
{
    #region Cashier
    public class Cashier
    {
        #region Member Variables
        protected int _id;
        protected string _Cashier;
        #endregion
        #region Constructors
        public Cashier() { }
        public Cashier(string Cashier)
        {
            this._Cashier=Cashier;
        }
        #endregion
        #region Public Properties
        public virtual int Id
        {
            get {return _id;}
            set {_id=value;}
        }
        public virtual string Cashier
        {
            get {return _Cashier;}
            set {_Cashier=value;}
        }
        #endregion
    }
    #endregion
}