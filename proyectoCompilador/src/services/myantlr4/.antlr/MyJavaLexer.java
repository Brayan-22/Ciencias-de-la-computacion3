// Generated from /home/alejandro/Documentos/semestres/novenoSemestre/ciencias3/Ciencias-de-la-computacion3/proyectoCompilador/src/services/myantlr4/MyJava.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MyJavaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PACKAGE=1, IMPORT=2, CLASS=3, PUBLIC=4, PROTECTED=5, PRIVATE=6, ABSTRACT=7, 
		STATIC=8, FINAL=9, BOOLEAN=10, CHAR=11, BYTE=12, SHORT=13, INT=14, LONG=15, 
		FLOAT=16, DOUBLE=17, STRING=18, PUNTO=19, PUNTOCOMA=20, COMA=21, IGUAL=22, 
		LLAVEIZQ=23, LLAVEDER=24, CORCHIZQ=25, CORCHDER=26, PARENIZQ=27, PARENDER=28, 
		DOSPUNTOS=29, VOID=30, MAIN=31, IF=32, ELSE=33, WHILE=34, DO=35, FOR=36, 
		MAYOR=37, MENOR=38, MAYORIGUAL=39, MENORIGUAL=40, IGUALIGUAL=41, DISTINTO=42, 
		MASMAS=43, MENOSMENOS=44, MAS=45, MENOS=46, ASTERISCO=47, DIV=48, SWITCH=49, 
		CASE=50, DEFAULT=51, BREAK=52, INTEGER_LITERAL=53, FLOAT_LITERAL=54, CHAR_LITERAL=55, 
		STRING_LITERAL=56, BOOLEAN_LITERAL=57, Identifier=58, COMMENT=59, LINE_COMMENT=60, 
		WS=61;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"PACKAGE", "IMPORT", "CLASS", "PUBLIC", "PROTECTED", "PRIVATE", "ABSTRACT", 
			"STATIC", "FINAL", "BOOLEAN", "CHAR", "BYTE", "SHORT", "INT", "LONG", 
			"FLOAT", "DOUBLE", "STRING", "PUNTO", "PUNTOCOMA", "COMA", "IGUAL", "LLAVEIZQ", 
			"LLAVEDER", "CORCHIZQ", "CORCHDER", "PARENIZQ", "PARENDER", "DOSPUNTOS", 
			"VOID", "MAIN", "IF", "ELSE", "WHILE", "DO", "FOR", "MAYOR", "MENOR", 
			"MAYORIGUAL", "MENORIGUAL", "IGUALIGUAL", "DISTINTO", "MASMAS", "MENOSMENOS", 
			"MAS", "MENOS", "ASTERISCO", "DIV", "SWITCH", "CASE", "DEFAULT", "BREAK", 
			"INTEGER_LITERAL", "FLOAT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", 
			"BOOLEAN_LITERAL", "Identifier", "JavaLetter", "JavaLetterOrDigit", "COMMENT", 
			"LINE_COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'package'", "'import'", "'class'", "'public'", "'protected'", 
			"'private'", "'abstract'", "'static'", "'final'", "'boolean'", "'char'", 
			"'byte'", "'short'", "'int'", "'long'", "'float'", "'double'", "'String'", 
			"'.'", "';'", "','", "'='", "'{'", "'}'", "'['", "']'", "'('", "')'", 
			"':'", "'void'", "'main'", "'if'", "'else'", "'while'", "'do'", "'for'", 
			"'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "'++'", "'--'", "'+'", 
			"'-'", "'*'", "'/'", "'switch'", "'case'", "'default'", "'break'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PACKAGE", "IMPORT", "CLASS", "PUBLIC", "PROTECTED", "PRIVATE", 
			"ABSTRACT", "STATIC", "FINAL", "BOOLEAN", "CHAR", "BYTE", "SHORT", "INT", 
			"LONG", "FLOAT", "DOUBLE", "STRING", "PUNTO", "PUNTOCOMA", "COMA", "IGUAL", 
			"LLAVEIZQ", "LLAVEDER", "CORCHIZQ", "CORCHDER", "PARENIZQ", "PARENDER", 
			"DOSPUNTOS", "VOID", "MAIN", "IF", "ELSE", "WHILE", "DO", "FOR", "MAYOR", 
			"MENOR", "MAYORIGUAL", "MENORIGUAL", "IGUALIGUAL", "DISTINTO", "MASMAS", 
			"MENOSMENOS", "MAS", "MENOS", "ASTERISCO", "DIV", "SWITCH", "CASE", "DEFAULT", 
			"BREAK", "INTEGER_LITERAL", "FLOAT_LITERAL", "CHAR_LITERAL", "STRING_LITERAL", 
			"BOOLEAN_LITERAL", "Identifier", "COMMENT", "LINE_COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MyJavaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyJava.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000=\u01b9\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r"+
		"\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001"+
		"!\u0001!\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001"+
		"#\u0001$\u0001$\u0001%\u0001%\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001"+
		"\'\u0001(\u0001(\u0001(\u0001)\u0001)\u0001)\u0001*\u0001*\u0001*\u0001"+
		"+\u0001+\u0001+\u0001,\u0001,\u0001-\u0001-\u0001.\u0001.\u0001/\u0001"+
		"/\u00010\u00010\u00010\u00010\u00010\u00010\u00010\u00011\u00011\u0001"+
		"1\u00011\u00011\u00012\u00012\u00012\u00012\u00012\u00012\u00012\u0001"+
		"2\u00013\u00013\u00013\u00013\u00013\u00013\u00014\u00044\u0167\b4\u000b"+
		"4\f4\u0168\u00015\u00045\u016c\b5\u000b5\f5\u016d\u00015\u00015\u0005"+
		"5\u0172\b5\n5\f5\u0175\t5\u00016\u00016\u00016\u00016\u00017\u00017\u0005"+
		"7\u017d\b7\n7\f7\u0180\t7\u00017\u00017\u00018\u00018\u00018\u00018\u0001"+
		"8\u00018\u00018\u00018\u00018\u00038\u018d\b8\u00019\u00019\u00059\u0191"+
		"\b9\n9\f9\u0194\t9\u0001:\u0001:\u0001;\u0001;\u0001<\u0001<\u0001<\u0001"+
		"<\u0005<\u019e\b<\n<\f<\u01a1\t<\u0001<\u0001<\u0001<\u0001<\u0001<\u0001"+
		"=\u0001=\u0001=\u0001=\u0005=\u01ac\b=\n=\f=\u01af\t=\u0001=\u0001=\u0001"+
		">\u0004>\u01b4\b>\u000b>\f>\u01b5\u0001>\u0001>\u0002\u017e\u019f\u0000"+
		"?\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"/\u00181\u00193\u001a5\u001b7\u001c9\u001d;\u001e=\u001f? A!C\"E#G$I%"+
		"K&M\'O(Q)S*U+W,Y-[.]/_0a1c2e3g4i5k6m7o8q9s:u\u0000w\u0000y;{<}=\u0001"+
		"\u0000\u0005\u0001\u000009\u0004\u0000$$AZ__az\u0005\u0000$$09AZ__az\u0002"+
		"\u0000\n\n\r\r\u0003\u0000\t\n\r\r  \u01bf\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001"+
		"\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000"+
		"\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000"+
		"\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001"+
		"\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001\u0000"+
		"\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000\u0000"+
		"\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000?"+
		"\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C\u0001\u0000"+
		"\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001\u0000\u0000\u0000"+
		"\u0000I\u0001\u0000\u0000\u0000\u0000K\u0001\u0000\u0000\u0000\u0000M"+
		"\u0001\u0000\u0000\u0000\u0000O\u0001\u0000\u0000\u0000\u0000Q\u0001\u0000"+
		"\u0000\u0000\u0000S\u0001\u0000\u0000\u0000\u0000U\u0001\u0000\u0000\u0000"+
		"\u0000W\u0001\u0000\u0000\u0000\u0000Y\u0001\u0000\u0000\u0000\u0000["+
		"\u0001\u0000\u0000\u0000\u0000]\u0001\u0000\u0000\u0000\u0000_\u0001\u0000"+
		"\u0000\u0000\u0000a\u0001\u0000\u0000\u0000\u0000c\u0001\u0000\u0000\u0000"+
		"\u0000e\u0001\u0000\u0000\u0000\u0000g\u0001\u0000\u0000\u0000\u0000i"+
		"\u0001\u0000\u0000\u0000\u0000k\u0001\u0000\u0000\u0000\u0000m\u0001\u0000"+
		"\u0000\u0000\u0000o\u0001\u0000\u0000\u0000\u0000q\u0001\u0000\u0000\u0000"+
		"\u0000s\u0001\u0000\u0000\u0000\u0000y\u0001\u0000\u0000\u0000\u0000{"+
		"\u0001\u0000\u0000\u0000\u0000}\u0001\u0000\u0000\u0000\u0001\u007f\u0001"+
		"\u0000\u0000\u0000\u0003\u0087\u0001\u0000\u0000\u0000\u0005\u008e\u0001"+
		"\u0000\u0000\u0000\u0007\u0094\u0001\u0000\u0000\u0000\t\u009b\u0001\u0000"+
		"\u0000\u0000\u000b\u00a5\u0001\u0000\u0000\u0000\r\u00ad\u0001\u0000\u0000"+
		"\u0000\u000f\u00b6\u0001\u0000\u0000\u0000\u0011\u00bd\u0001\u0000\u0000"+
		"\u0000\u0013\u00c3\u0001\u0000\u0000\u0000\u0015\u00cb\u0001\u0000\u0000"+
		"\u0000\u0017\u00d0\u0001\u0000\u0000\u0000\u0019\u00d5\u0001\u0000\u0000"+
		"\u0000\u001b\u00db\u0001\u0000\u0000\u0000\u001d\u00df\u0001\u0000\u0000"+
		"\u0000\u001f\u00e4\u0001\u0000\u0000\u0000!\u00ea\u0001\u0000\u0000\u0000"+
		"#\u00f1\u0001\u0000\u0000\u0000%\u00f8\u0001\u0000\u0000\u0000\'\u00fa"+
		"\u0001\u0000\u0000\u0000)\u00fc\u0001\u0000\u0000\u0000+\u00fe\u0001\u0000"+
		"\u0000\u0000-\u0100\u0001\u0000\u0000\u0000/\u0102\u0001\u0000\u0000\u0000"+
		"1\u0104\u0001\u0000\u0000\u00003\u0106\u0001\u0000\u0000\u00005\u0108"+
		"\u0001\u0000\u0000\u00007\u010a\u0001\u0000\u0000\u00009\u010c\u0001\u0000"+
		"\u0000\u0000;\u010e\u0001\u0000\u0000\u0000=\u0113\u0001\u0000\u0000\u0000"+
		"?\u0118\u0001\u0000\u0000\u0000A\u011b\u0001\u0000\u0000\u0000C\u0120"+
		"\u0001\u0000\u0000\u0000E\u0126\u0001\u0000\u0000\u0000G\u0129\u0001\u0000"+
		"\u0000\u0000I\u012d\u0001\u0000\u0000\u0000K\u012f\u0001\u0000\u0000\u0000"+
		"M\u0131\u0001\u0000\u0000\u0000O\u0134\u0001\u0000\u0000\u0000Q\u0137"+
		"\u0001\u0000\u0000\u0000S\u013a\u0001\u0000\u0000\u0000U\u013d\u0001\u0000"+
		"\u0000\u0000W\u0140\u0001\u0000\u0000\u0000Y\u0143\u0001\u0000\u0000\u0000"+
		"[\u0145\u0001\u0000\u0000\u0000]\u0147\u0001\u0000\u0000\u0000_\u0149"+
		"\u0001\u0000\u0000\u0000a\u014b\u0001\u0000\u0000\u0000c\u0152\u0001\u0000"+
		"\u0000\u0000e\u0157\u0001\u0000\u0000\u0000g\u015f\u0001\u0000\u0000\u0000"+
		"i\u0166\u0001\u0000\u0000\u0000k\u016b\u0001\u0000\u0000\u0000m\u0176"+
		"\u0001\u0000\u0000\u0000o\u017a\u0001\u0000\u0000\u0000q\u018c\u0001\u0000"+
		"\u0000\u0000s\u018e\u0001\u0000\u0000\u0000u\u0195\u0001\u0000\u0000\u0000"+
		"w\u0197\u0001\u0000\u0000\u0000y\u0199\u0001\u0000\u0000\u0000{\u01a7"+
		"\u0001\u0000\u0000\u0000}\u01b3\u0001\u0000\u0000\u0000\u007f\u0080\u0005"+
		"p\u0000\u0000\u0080\u0081\u0005a\u0000\u0000\u0081\u0082\u0005c\u0000"+
		"\u0000\u0082\u0083\u0005k\u0000\u0000\u0083\u0084\u0005a\u0000\u0000\u0084"+
		"\u0085\u0005g\u0000\u0000\u0085\u0086\u0005e\u0000\u0000\u0086\u0002\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0005i\u0000\u0000\u0088\u0089\u0005m\u0000"+
		"\u0000\u0089\u008a\u0005p\u0000\u0000\u008a\u008b\u0005o\u0000\u0000\u008b"+
		"\u008c\u0005r\u0000\u0000\u008c\u008d\u0005t\u0000\u0000\u008d\u0004\u0001"+
		"\u0000\u0000\u0000\u008e\u008f\u0005c\u0000\u0000\u008f\u0090\u0005l\u0000"+
		"\u0000\u0090\u0091\u0005a\u0000\u0000\u0091\u0092\u0005s\u0000\u0000\u0092"+
		"\u0093\u0005s\u0000\u0000\u0093\u0006\u0001\u0000\u0000\u0000\u0094\u0095"+
		"\u0005p\u0000\u0000\u0095\u0096\u0005u\u0000\u0000\u0096\u0097\u0005b"+
		"\u0000\u0000\u0097\u0098\u0005l\u0000\u0000\u0098\u0099\u0005i\u0000\u0000"+
		"\u0099\u009a\u0005c\u0000\u0000\u009a\b\u0001\u0000\u0000\u0000\u009b"+
		"\u009c\u0005p\u0000\u0000\u009c\u009d\u0005r\u0000\u0000\u009d\u009e\u0005"+
		"o\u0000\u0000\u009e\u009f\u0005t\u0000\u0000\u009f\u00a0\u0005e\u0000"+
		"\u0000\u00a0\u00a1\u0005c\u0000\u0000\u00a1\u00a2\u0005t\u0000\u0000\u00a2"+
		"\u00a3\u0005e\u0000\u0000\u00a3\u00a4\u0005d\u0000\u0000\u00a4\n\u0001"+
		"\u0000\u0000\u0000\u00a5\u00a6\u0005p\u0000\u0000\u00a6\u00a7\u0005r\u0000"+
		"\u0000\u00a7\u00a8\u0005i\u0000\u0000\u00a8\u00a9\u0005v\u0000\u0000\u00a9"+
		"\u00aa\u0005a\u0000\u0000\u00aa\u00ab\u0005t\u0000\u0000\u00ab\u00ac\u0005"+
		"e\u0000\u0000\u00ac\f\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005a\u0000"+
		"\u0000\u00ae\u00af\u0005b\u0000\u0000\u00af\u00b0\u0005s\u0000\u0000\u00b0"+
		"\u00b1\u0005t\u0000\u0000\u00b1\u00b2\u0005r\u0000\u0000\u00b2\u00b3\u0005"+
		"a\u0000\u0000\u00b3\u00b4\u0005c\u0000\u0000\u00b4\u00b5\u0005t\u0000"+
		"\u0000\u00b5\u000e\u0001\u0000\u0000\u0000\u00b6\u00b7\u0005s\u0000\u0000"+
		"\u00b7\u00b8\u0005t\u0000\u0000\u00b8\u00b9\u0005a\u0000\u0000\u00b9\u00ba"+
		"\u0005t\u0000\u0000\u00ba\u00bb\u0005i\u0000\u0000\u00bb\u00bc\u0005c"+
		"\u0000\u0000\u00bc\u0010\u0001\u0000\u0000\u0000\u00bd\u00be\u0005f\u0000"+
		"\u0000\u00be\u00bf\u0005i\u0000\u0000\u00bf\u00c0\u0005n\u0000\u0000\u00c0"+
		"\u00c1\u0005a\u0000\u0000\u00c1\u00c2\u0005l\u0000\u0000\u00c2\u0012\u0001"+
		"\u0000\u0000\u0000\u00c3\u00c4\u0005b\u0000\u0000\u00c4\u00c5\u0005o\u0000"+
		"\u0000\u00c5\u00c6\u0005o\u0000\u0000\u00c6\u00c7\u0005l\u0000\u0000\u00c7"+
		"\u00c8\u0005e\u0000\u0000\u00c8\u00c9\u0005a\u0000\u0000\u00c9\u00ca\u0005"+
		"n\u0000\u0000\u00ca\u0014\u0001\u0000\u0000\u0000\u00cb\u00cc\u0005c\u0000"+
		"\u0000\u00cc\u00cd\u0005h\u0000\u0000\u00cd\u00ce\u0005a\u0000\u0000\u00ce"+
		"\u00cf\u0005r\u0000\u0000\u00cf\u0016\u0001\u0000\u0000\u0000\u00d0\u00d1"+
		"\u0005b\u0000\u0000\u00d1\u00d2\u0005y\u0000\u0000\u00d2\u00d3\u0005t"+
		"\u0000\u0000\u00d3\u00d4\u0005e\u0000\u0000\u00d4\u0018\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d6\u0005s\u0000\u0000\u00d6\u00d7\u0005h\u0000\u0000\u00d7"+
		"\u00d8\u0005o\u0000\u0000\u00d8\u00d9\u0005r\u0000\u0000\u00d9\u00da\u0005"+
		"t\u0000\u0000\u00da\u001a\u0001\u0000\u0000\u0000\u00db\u00dc\u0005i\u0000"+
		"\u0000\u00dc\u00dd\u0005n\u0000\u0000\u00dd\u00de\u0005t\u0000\u0000\u00de"+
		"\u001c\u0001\u0000\u0000\u0000\u00df\u00e0\u0005l\u0000\u0000\u00e0\u00e1"+
		"\u0005o\u0000\u0000\u00e1\u00e2\u0005n\u0000\u0000\u00e2\u00e3\u0005g"+
		"\u0000\u0000\u00e3\u001e\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005f\u0000"+
		"\u0000\u00e5\u00e6\u0005l\u0000\u0000\u00e6\u00e7\u0005o\u0000\u0000\u00e7"+
		"\u00e8\u0005a\u0000\u0000\u00e8\u00e9\u0005t\u0000\u0000\u00e9 \u0001"+
		"\u0000\u0000\u0000\u00ea\u00eb\u0005d\u0000\u0000\u00eb\u00ec\u0005o\u0000"+
		"\u0000\u00ec\u00ed\u0005u\u0000\u0000\u00ed\u00ee\u0005b\u0000\u0000\u00ee"+
		"\u00ef\u0005l\u0000\u0000\u00ef\u00f0\u0005e\u0000\u0000\u00f0\"\u0001"+
		"\u0000\u0000\u0000\u00f1\u00f2\u0005S\u0000\u0000\u00f2\u00f3\u0005t\u0000"+
		"\u0000\u00f3\u00f4\u0005r\u0000\u0000\u00f4\u00f5\u0005i\u0000\u0000\u00f5"+
		"\u00f6\u0005n\u0000\u0000\u00f6\u00f7\u0005g\u0000\u0000\u00f7$\u0001"+
		"\u0000\u0000\u0000\u00f8\u00f9\u0005.\u0000\u0000\u00f9&\u0001\u0000\u0000"+
		"\u0000\u00fa\u00fb\u0005;\u0000\u0000\u00fb(\u0001\u0000\u0000\u0000\u00fc"+
		"\u00fd\u0005,\u0000\u0000\u00fd*\u0001\u0000\u0000\u0000\u00fe\u00ff\u0005"+
		"=\u0000\u0000\u00ff,\u0001\u0000\u0000\u0000\u0100\u0101\u0005{\u0000"+
		"\u0000\u0101.\u0001\u0000\u0000\u0000\u0102\u0103\u0005}\u0000\u0000\u0103"+
		"0\u0001\u0000\u0000\u0000\u0104\u0105\u0005[\u0000\u0000\u01052\u0001"+
		"\u0000\u0000\u0000\u0106\u0107\u0005]\u0000\u0000\u01074\u0001\u0000\u0000"+
		"\u0000\u0108\u0109\u0005(\u0000\u0000\u01096\u0001\u0000\u0000\u0000\u010a"+
		"\u010b\u0005)\u0000\u0000\u010b8\u0001\u0000\u0000\u0000\u010c\u010d\u0005"+
		":\u0000\u0000\u010d:\u0001\u0000\u0000\u0000\u010e\u010f\u0005v\u0000"+
		"\u0000\u010f\u0110\u0005o\u0000\u0000\u0110\u0111\u0005i\u0000\u0000\u0111"+
		"\u0112\u0005d\u0000\u0000\u0112<\u0001\u0000\u0000\u0000\u0113\u0114\u0005"+
		"m\u0000\u0000\u0114\u0115\u0005a\u0000\u0000\u0115\u0116\u0005i\u0000"+
		"\u0000\u0116\u0117\u0005n\u0000\u0000\u0117>\u0001\u0000\u0000\u0000\u0118"+
		"\u0119\u0005i\u0000\u0000\u0119\u011a\u0005f\u0000\u0000\u011a@\u0001"+
		"\u0000\u0000\u0000\u011b\u011c\u0005e\u0000\u0000\u011c\u011d\u0005l\u0000"+
		"\u0000\u011d\u011e\u0005s\u0000\u0000\u011e\u011f\u0005e\u0000\u0000\u011f"+
		"B\u0001\u0000\u0000\u0000\u0120\u0121\u0005w\u0000\u0000\u0121\u0122\u0005"+
		"h\u0000\u0000\u0122\u0123\u0005i\u0000\u0000\u0123\u0124\u0005l\u0000"+
		"\u0000\u0124\u0125\u0005e\u0000\u0000\u0125D\u0001\u0000\u0000\u0000\u0126"+
		"\u0127\u0005d\u0000\u0000\u0127\u0128\u0005o\u0000\u0000\u0128F\u0001"+
		"\u0000\u0000\u0000\u0129\u012a\u0005f\u0000\u0000\u012a\u012b\u0005o\u0000"+
		"\u0000\u012b\u012c\u0005r\u0000\u0000\u012cH\u0001\u0000\u0000\u0000\u012d"+
		"\u012e\u0005>\u0000\u0000\u012eJ\u0001\u0000\u0000\u0000\u012f\u0130\u0005"+
		"<\u0000\u0000\u0130L\u0001\u0000\u0000\u0000\u0131\u0132\u0005>\u0000"+
		"\u0000\u0132\u0133\u0005=\u0000\u0000\u0133N\u0001\u0000\u0000\u0000\u0134"+
		"\u0135\u0005<\u0000\u0000\u0135\u0136\u0005=\u0000\u0000\u0136P\u0001"+
		"\u0000\u0000\u0000\u0137\u0138\u0005=\u0000\u0000\u0138\u0139\u0005=\u0000"+
		"\u0000\u0139R\u0001\u0000\u0000\u0000\u013a\u013b\u0005!\u0000\u0000\u013b"+
		"\u013c\u0005=\u0000\u0000\u013cT\u0001\u0000\u0000\u0000\u013d\u013e\u0005"+
		"+\u0000\u0000\u013e\u013f\u0005+\u0000\u0000\u013fV\u0001\u0000\u0000"+
		"\u0000\u0140\u0141\u0005-\u0000\u0000\u0141\u0142\u0005-\u0000\u0000\u0142"+
		"X\u0001\u0000\u0000\u0000\u0143\u0144\u0005+\u0000\u0000\u0144Z\u0001"+
		"\u0000\u0000\u0000\u0145\u0146\u0005-\u0000\u0000\u0146\\\u0001\u0000"+
		"\u0000\u0000\u0147\u0148\u0005*\u0000\u0000\u0148^\u0001\u0000\u0000\u0000"+
		"\u0149\u014a\u0005/\u0000\u0000\u014a`\u0001\u0000\u0000\u0000\u014b\u014c"+
		"\u0005s\u0000\u0000\u014c\u014d\u0005w\u0000\u0000\u014d\u014e\u0005i"+
		"\u0000\u0000\u014e\u014f\u0005t\u0000\u0000\u014f\u0150\u0005c\u0000\u0000"+
		"\u0150\u0151\u0005h\u0000\u0000\u0151b\u0001\u0000\u0000\u0000\u0152\u0153"+
		"\u0005c\u0000\u0000\u0153\u0154\u0005a\u0000\u0000\u0154\u0155\u0005s"+
		"\u0000\u0000\u0155\u0156\u0005e\u0000\u0000\u0156d\u0001\u0000\u0000\u0000"+
		"\u0157\u0158\u0005d\u0000\u0000\u0158\u0159\u0005e\u0000\u0000\u0159\u015a"+
		"\u0005f\u0000\u0000\u015a\u015b\u0005a\u0000\u0000\u015b\u015c\u0005u"+
		"\u0000\u0000\u015c\u015d\u0005l\u0000\u0000\u015d\u015e\u0005t\u0000\u0000"+
		"\u015ef\u0001\u0000\u0000\u0000\u015f\u0160\u0005b\u0000\u0000\u0160\u0161"+
		"\u0005r\u0000\u0000\u0161\u0162\u0005e\u0000\u0000\u0162\u0163\u0005a"+
		"\u0000\u0000\u0163\u0164\u0005k\u0000\u0000\u0164h\u0001\u0000\u0000\u0000"+
		"\u0165\u0167\u0007\u0000\u0000\u0000\u0166\u0165\u0001\u0000\u0000\u0000"+
		"\u0167\u0168\u0001\u0000\u0000\u0000\u0168\u0166\u0001\u0000\u0000\u0000"+
		"\u0168\u0169\u0001\u0000\u0000\u0000\u0169j\u0001\u0000\u0000\u0000\u016a"+
		"\u016c\u0007\u0000\u0000\u0000\u016b\u016a\u0001\u0000\u0000\u0000\u016c"+
		"\u016d\u0001\u0000\u0000\u0000\u016d\u016b\u0001\u0000\u0000\u0000\u016d"+
		"\u016e\u0001\u0000\u0000\u0000\u016e\u016f\u0001\u0000\u0000\u0000\u016f"+
		"\u0173\u0005.\u0000\u0000\u0170\u0172\u0007\u0000\u0000\u0000\u0171\u0170"+
		"\u0001\u0000\u0000\u0000\u0172\u0175\u0001\u0000\u0000\u0000\u0173\u0171"+
		"\u0001\u0000\u0000\u0000\u0173\u0174\u0001\u0000\u0000\u0000\u0174l\u0001"+
		"\u0000\u0000\u0000\u0175\u0173\u0001\u0000\u0000\u0000\u0176\u0177\u0005"+
		"\'\u0000\u0000\u0177\u0178\t\u0000\u0000\u0000\u0178\u0179\u0005\'\u0000"+
		"\u0000\u0179n\u0001\u0000\u0000\u0000\u017a\u017e\u0005\"\u0000\u0000"+
		"\u017b\u017d\t\u0000\u0000\u0000\u017c\u017b\u0001\u0000\u0000\u0000\u017d"+
		"\u0180\u0001\u0000\u0000\u0000\u017e\u017f\u0001\u0000\u0000\u0000\u017e"+
		"\u017c\u0001\u0000\u0000\u0000\u017f\u0181\u0001\u0000\u0000\u0000\u0180"+
		"\u017e\u0001\u0000\u0000\u0000\u0181\u0182\u0005\"\u0000\u0000\u0182p"+
		"\u0001\u0000\u0000\u0000\u0183\u0184\u0005t\u0000\u0000\u0184\u0185\u0005"+
		"r\u0000\u0000\u0185\u0186\u0005u\u0000\u0000\u0186\u018d\u0005e\u0000"+
		"\u0000\u0187\u0188\u0005f\u0000\u0000\u0188\u0189\u0005a\u0000\u0000\u0189"+
		"\u018a\u0005l\u0000\u0000\u018a\u018b\u0005s\u0000\u0000\u018b\u018d\u0005"+
		"e\u0000\u0000\u018c\u0183\u0001\u0000\u0000\u0000\u018c\u0187\u0001\u0000"+
		"\u0000\u0000\u018dr\u0001\u0000\u0000\u0000\u018e\u0192\u0003u:\u0000"+
		"\u018f\u0191\u0003w;\u0000\u0190\u018f\u0001\u0000\u0000\u0000\u0191\u0194"+
		"\u0001\u0000\u0000\u0000\u0192\u0190\u0001\u0000\u0000\u0000\u0192\u0193"+
		"\u0001\u0000\u0000\u0000\u0193t\u0001\u0000\u0000\u0000\u0194\u0192\u0001"+
		"\u0000\u0000\u0000\u0195\u0196\u0007\u0001\u0000\u0000\u0196v\u0001\u0000"+
		"\u0000\u0000\u0197\u0198\u0007\u0002\u0000\u0000\u0198x\u0001\u0000\u0000"+
		"\u0000\u0199\u019a\u0005/\u0000\u0000\u019a\u019b\u0005*\u0000\u0000\u019b"+
		"\u019f\u0001\u0000\u0000\u0000\u019c\u019e\t\u0000\u0000\u0000\u019d\u019c"+
		"\u0001\u0000\u0000\u0000\u019e\u01a1\u0001\u0000\u0000\u0000\u019f\u01a0"+
		"\u0001\u0000\u0000\u0000\u019f\u019d\u0001\u0000\u0000\u0000\u01a0\u01a2"+
		"\u0001\u0000\u0000\u0000\u01a1\u019f\u0001\u0000\u0000\u0000\u01a2\u01a3"+
		"\u0005*\u0000\u0000\u01a3\u01a4\u0005/\u0000\u0000\u01a4\u01a5\u0001\u0000"+
		"\u0000\u0000\u01a5\u01a6\u0006<\u0000\u0000\u01a6z\u0001\u0000\u0000\u0000"+
		"\u01a7\u01a8\u0005/\u0000\u0000\u01a8\u01a9\u0005/\u0000\u0000\u01a9\u01ad"+
		"\u0001\u0000\u0000\u0000\u01aa\u01ac\b\u0003\u0000\u0000\u01ab\u01aa\u0001"+
		"\u0000\u0000\u0000\u01ac\u01af\u0001\u0000\u0000\u0000\u01ad\u01ab\u0001"+
		"\u0000\u0000\u0000\u01ad\u01ae\u0001\u0000\u0000\u0000\u01ae\u01b0\u0001"+
		"\u0000\u0000\u0000\u01af\u01ad\u0001\u0000\u0000\u0000\u01b0\u01b1\u0006"+
		"=\u0000\u0000\u01b1|\u0001\u0000\u0000\u0000\u01b2\u01b4\u0007\u0004\u0000"+
		"\u0000\u01b3\u01b2\u0001\u0000\u0000\u0000\u01b4\u01b5\u0001\u0000\u0000"+
		"\u0000\u01b5\u01b3\u0001\u0000\u0000\u0000\u01b5\u01b6\u0001\u0000\u0000"+
		"\u0000\u01b6\u01b7\u0001\u0000\u0000\u0000\u01b7\u01b8\u0006>\u0001\u0000"+
		"\u01b8~\u0001\u0000\u0000\u0000\n\u0000\u0168\u016d\u0173\u017e\u018c"+
		"\u0192\u019f\u01ad\u01b5\u0002\u0000\u0001\u0000\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}