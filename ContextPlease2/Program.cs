using System;
using System.IO;

namespace ContextPlease2
{
    class Program
    {
        
        /// <summary>
        /// Entry point function
        /// </summary>
        /// <param name="input">Path to the input JSON configuration file</param>
        /// <param name="output">Path to the generated REG files</param>
        /// <param name="keepOld">Should pre-existing registry keys be kept when writing new ones?</param>
        /// <param name="makeUninstaller">Should a removal registry script be generated?</param>
        static void Main(
            string input,
            string? output,
            bool keepOld = false,
            bool makeUninstaller = true)
        {
            try
            {
                Configuration config = ReadArguments(input, output, keepOld, makeUninstaller);
                ContextPlease contextPlease = new(config);
                
                contextPlease.Run();
            }
            catch (Exception e)
            {
                Console.Error.WriteLine(e.Message);
                Environment.Exit(-1);
            }
        }

        /// <summary>
        /// Validates and normalizes command line arguments and assembles a settings file.
        /// </summary>
        /// <param name="input">Path to input file</param>
        /// <param name="output">Path to output file</param>
        /// <param name="keepOld">Should pre-existing registry keys be kept when writing new ones?</param>
        /// <param name="makeUninstaller">Should a removal registry script be generated?</param>
        /// <returns>Settings object with the program settings</returns>
        /// <exception cref="ArgumentNullException">If input is null</exception>
        /// <exception cref="FileNotFoundException">If input file cannot be found</exception>
        private static Configuration ReadArguments(
            string input,
            string? output,
            bool keepOld,
            bool makeUninstaller)
        {
            if (input == null)
            {
                throw new ArgumentNullException(
                    paramName: nameof(input),
                    message: "An input file must be specified");
            }

            if (!File.Exists(input))
            {
                throw new FileNotFoundException(
                    fileName: input,
                    message: $"Input file could not be found: {input}");
            }

            output = NormalizeOutputWith(output, input);

            return new Configuration(input, output, keepOld, makeUninstaller);
        }

        private static string NormalizeOutputWith(string? output, string input)
        {
            output ??= Path.GetFileNameWithoutExtension(input);
            
            if (Path.EndsInDirectorySeparator(output))
            {
                output = Path.Combine(output, Path.GetFileNameWithoutExtension(input));
            }

            if (Path.GetExtension(output) == ".reg")
            {
                output = Path.GetFileNameWithoutExtension(output);
            }

            return output;
        }
    }
}
