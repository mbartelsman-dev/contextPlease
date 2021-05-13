using System.Linq;

namespace ContextPlease2.Extensions
{
    public static class StringExtensions
    {
        /// <summary>
        /// Produces an ascii string with no spaces
        /// </summary>
        /// <param name="inputString">The string to be sanitized</param>
        /// <returns>The sanitized string</returns>
        public static string ToSafeAscii(this string inputString)
        {   
            string EscapeChar(char inputChar)
            {
                if (inputChar >= 128)
                {
                    return $@"\u{(int) inputChar:x4}";
                }
                return inputChar.ToString();
            }

            return string
                .Concat(inputString.Select(EscapeChar))
                .Replace(" ", "");
        }
    }
}
