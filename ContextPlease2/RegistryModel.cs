namespace ContextPlease2
{
    public class RegistryModel
    {

        /// <summary>
        /// Creates a new RegistryModel object from a given JsonModel
        /// </summary>
        /// <returns>The new RegistryModel object</returns>
        public static RegistryModel FromJsonModel(JsonModel jsonModel)
        {
            throw new System.NotImplementedException();
        }
        
        public void SerializeInstaller(string path, bool keepOld)
        {
            if (keepOld)
            {
                AdditiveInstaller(path);
            }
            else
            {
                CleanInstaller(path);
            }
        }

        public void SerializeUninstaller(string path)
        {
            throw new System.NotImplementedException();
        }

        private void CleanInstaller(string path)
        {
            throw new System.NotImplementedException();
        }

        private void AdditiveInstaller(string path)
        {
            throw new System.NotImplementedException();
        }
    }
}
