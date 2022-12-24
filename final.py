from experta import *
import pyarabic.araby as ar
import pyquran as q

global t
global Verse
global s
global result


s = 0
Verse = 0
t = q.quran.get_verse(s, Verse, True)
result = []


class text(Fact):
    pass


class Iqlab(Fact):
    pass


class IdghaamWithGhunnah(Fact):
    pass


class IdghaamWithOutGhunnah(Fact):
    pass


class Ikhfa(Fact):
    pass


class QalqalahSughraa(Fact):
    pass


class QalqalahKubraa(Fact):
    pass


class LafzGlalahMuraqaq(Fact):
    pass


class LafzGlalahMufakham(Fact):
    pass


class Ezhar(Fact):
    pass


class Madd(Fact):
    pass


class MaddBadal(Fact):
    pass


class EzharHalqi(Fact):
    pass


class MaddEwad(Fact):
    pass


class TfkemAlRaa(Fact):
    pass


class TarkekAlRaa(Fact):
    pass


class TafkemAlEstalaa(Fact):
    pass


class ikhfaa_shafawi(Fact):
    pass


class idgam_shafawi(Fact):
    pass


class izhar_shafawi(Fact):
    pass


class mad_wajeb_motasel(Fact):
    pass


class mad_jaaez_monfasel(Fact):
    pass


class mad_alleen(Fact):
    pass


class mad_lazem_kaleme_mothqal(Fact):
    pass


class mad_lazem_kaleme_mokhafaf(Fact):
    pass


class mad_lazem_harfi_mothqal(Fact):
    pass


class mad_lazem_harfi_mokhafaf(Fact):
    pass


class TafkemAlAlef(Fact):
    pass


class TarkekAlAlef(Fact):
    pass


class LamAlmarefa(Fact):
    pass


class madtmken(Fact):
    pass


class MaddAredLilsukun(Fact):
    pass


class madsela1(Fact):
    pass


class madsela2(Fact):
    pass


class Quran(KnowledgeEngine):
    @DefFacts()
    def initial_fact(self):
        yield Fact(a='input')
        yield text(v=Verse)

    @Rule(TafkemAlAlef(a='True'))
    def TafkemAlAlef(self):
        print('الحكم : تفخيم الالف ', t)

    @Rule(TarkekAlAlef(a='True'))
    def TarkekAlAlef(self):
        print('الحكم : ترقيق الالف ', t)

    @Rule(LamAlmarefa(a='True'))
    def LamAlmarefa(self):
        print('الحكم : لام المعرفة ', t)

    @Rule(Iqlab(a='True'))
    def Iqlab(self):
        print("الحكم اقلاب في", t)

    @Rule(IdghaamWithGhunnah(a='True'))
    def IdghaamWithGhunnah(self):
        print("إدغام بغنة", t)

    @Rule(IdghaamWithOutGhunnah(a='True'))
    def IdghaamWithOutGhunnah(self):
        print("إدغام بلا غنة", t)

    @Rule(Ikhfa(a='True'))
    def Ikhfa(self):
        print("الحكم إخفاء", t)

    @Rule(QalqalahSughraa(a='True'))
    def QalqalahSughraa(self):
        print("الحكم قلقلة صغرى ", t)

    @Rule(QalqalahKubraa(a='True'))
    def QalqalahKubraa(self):
        print("الحكم قلقلة كبرى", t)

    @Rule(LafzGlalahMuraqaq(a='True'))
    def LafzGlalahMuraqaq(self):
        print("الحكم لفظ جلالة مرقق", t)

    @Rule(LafzGlalahMufakham(a='True'))
    def LafzGlalahMufakham(self):
        print("الحكم لفظ جلالة مفخم", t)

    @Rule(Madd(a='True'))
    def Madd(self):
        print("الحكم مد طبيعي في ", t)

    @Rule(MaddBadal(a='True'))
    def MaddBadal(self):
        print("الحكم مد بدل في ", t)

    @Rule(EzharHalqi(a='True'))
    def EzharHalqi(self):
        print("الحكم إظهار مطلق في ", t)

    @Rule(MaddEwad(a='True'))
    def MaddEwad(self):
        print("الحكم مد عوض في ", t)

    @Rule(TfkemAlRaa(a='True'))
    def TfkemAlRaa(self):
        print("الحكم : راء مفخمة ", t)

    @Rule(TarkekAlRaa(a='True'))
    def TarkekAlRaa(self):
        print('الحكم : الراء مرققة', t)

    @Rule(TafkemAlEstalaa(a='True'))
    def TafkemAlEstalaa(self):
        print('الحكم تفخيم حرف استعلاء (خص ضغط قظ)', t)

    @Rule(ikhfaa_shafawi(a='True'))
    def ikhfaa_shafawi(self):
        print("الحكم اخفاء شفوي")

    @Rule(idgam_shafawi(a='True'))
    def idgam_shafawi(self):
        print("الحكم ادغام شفوي")

    @Rule(izhar_shafawi(a='True'))
    def izhar_shafawi(self):
        print("الحكم اظهار شفوي")

    @Rule(mad_wajeb_motasel(a='True'))
    def mad_wajeb_motasel(self):
        print("الحكم مد واجب متصل")

    @Rule(mad_jaaez_monfasel(a='True'))
    def mad_jaaez_monfasel(self):
        print("الحكم مد جائز منفصل")

    @Rule(mad_alleen(a='True'))
    def mad_alleen(self):
        print("الحكم مد اللين")

    @Rule(mad_lazem_kaleme_mothqal(a='True'))
    def mad_lazem_kaleme_mothqal(self):
        print("الحكم مد لازم كلمي مثقل")

    @Rule(mad_lazem_kaleme_mokhafaf(a='True'))
    def mad_lazem_kaleme_mokhafaf(self):
        print("الحكم مد لازم كلمي مخفف")

    @Rule(mad_lazem_harfi_mothqal(a='True'))
    def mad_lazem_harfi_mothqal(self):
        print("الحكم مد لازم حرفي مثقل")

    @Rule(mad_lazem_harfi_mokhafaf(a='True'))
    def mad_lazem_harfi_mokhafaf(self):
        print("الحكم مد لازم حرفي مخفف")

    @Rule(madtmken(a='True'))
    def madtmken(self):
        print("الحكم مد تمكين في ", t)

    @Rule(MaddAredLilsukun(a='True'))
    def MaddAredLilsukun(self):
        print("الحكم مد عارض للسكون في ", t)

    @Rule(madsela1(a='True'))
    def madsela1(self):
        print("الحكم مد صلة صغرى في ", t)

    @Rule(madsela2(a='True'))
    def madsela2(self):
        print("الحكم مد صلة كبرى في ", t)

    @Rule(Ezhar(a='True'))
    def Ezhar(self):
        print("الحكم هو اظهار في", t)

    @Rule()
    def findEzhar(self):
        n1 = []
        d1 = []
        f1 = []
        k1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
            if char == ar.DAMMATAN:
                d1.append(i)
            if char == ar.FATHATAN:
                f1.append(i)
            if char == ar.KASRATAN:
                k1.append(i)
        for n in n1:
            if ar.is_sukun(t[n + 1]) and (t[n + 2] == ' '):
                if (n + 4 < len(t)) and (
                        t[n + 3] == ar.GHAIN or t[n + 3] == ar.ALEF_HAMZA_BELOW or t[n + 3] == ar.HAMZA or t[
                    n + 3] == ar.ALEF or t[n + 3] == ar.ALEF_HAMZA_ABOVE or t[
                            n + 3] == ar.AIN or t[n + 3] == ar.HAH or t[n + 3] == ar.HEH or t[n + 3] == ar.KHAH):
                    self.declare(Ezhar(a='True'))
                    print(t[n - 1:n + 4])
                    ss=t[n - 1:n + 4]
                    result.append("الحكم الحكم اظهار "+'('+ss+')')

            elif t[n + 1] == ' ':
                if (n + 3 < len(t)) and (
                        t[n + 2] == ar.GHAIN or t[n + 2] == ar.ALEF_HAMZA_BELOW or t[n + 2] == ar.HAMZA or t[
                    n + 2] == ar.ALEF or t[n + 2] == ar.ALEF_HAMZA_ABOVE or t[
                            n + 2] == ar.AIN or t[n + 2] == ar.HAH or t[n + 2] == ar.HEH or t[n + 2] == ar.KHAH):
                    self.declare(Ezhar(a='True'))
                    print(t[n - 1:n + 3])
                    ss=t[n - 1:n + 3]
                    result.append("الحكم الحكم اظهار "+'('+ss+')')

            elif ar.is_sukun(t[n + 1]):
                if (n + 3 < len(t)) and (
                        t[n + 2] == ar.GHAIN or t[n + 2] == ar.ALEF_HAMZA_BELOW or t[n + 2] == ar.HAMZA or t[
                    n + 2] == ar.ALEF or t[n + 2] == ar.ALEF_HAMZA_ABOVE or t[
                            n + 2] == ar.AIN or t[n + 2] == ar.HAH or t[n + 2] == ar.HEH or t[n + 2] == ar.KHAH):
                    self.declare(Ezhar(a='True'))
                    print(t[n - 1:n + 3])
                    ss=t[n - 1:n + 3]
                    result.append("الحكم الحكم اظهار "+'('+ss+')')

            elif (n + 2 < len(t)) and (
                    t[n + 1] == ar.GHAIN or t[n + 1] == ar.HAMZA or t[n + 1] == ar.ALEF_HAMZA_ABOVE or t[
                n + 1] == ar.ALEF_HAMZA_BELOW or t[
                        n + 1] == ar.AIN or t[n + 1] == ar.HAH or t[n + 1] == ar.ALEF or t[n + 1] == ar.HEH or t[
                        n + 1] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[n - 1:n + 2])
                ss = t[n - 1:n + 2]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
        for d in d1:
            if (d + 3 < len(t)) and (t[d + 2] == ar.GHAIN or t[d + 2] == ar.HAMZA or t[d + 2] == ar.ALEF or t[
                d + 2] == ar.ALEF_HAMZA_ABOVE
                                     or t[d + 2] == ar.ALEF_HAMZA_BELOW or t[d + 2] == ar.AIN or t[d + 2] == ar.HAH or
                                     t[d + 2] == ar.HEH or t[d + 2] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[d - 1:d + 3])
                ss = t[d - 1:d + 3]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
            if (d + 4 < len(t)) and (t[d + 1] == ar.ALEF) and (t[d + 2] == ' ') and (
                    t[d + 3] == ar.GHAIN or t[d + 3] == ar.ALEF_HAMZA_BELOW or t[d + 3] == ar.ALEF or t[
                d + 3] == ar.HAMZA or t[d + 3] == ar.ALEF_HAMZA_ABOVE or t[d + 3] == ar.AIN or t[d + 3] == ar.HAH or t[
                        d + 3] == ar.HEH or t[d + 3] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[d - 1:d + 4])
                ss = t[d - 1:d + 4]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
        for f in f1:
            if (f + 3 < len(t)) and (t[f + 2] == ar.GHAIN or t[f + 2] == ar.HAMZA or t[f + 2] == ar.ALEF or t[
                f + 2] == ar.ALEF_HAMZA_ABOVE or t[f + 2] == ar.ALEF_HAMZA_BELOW or t[f + 2] == ar.ALEF_HAMZA_BELOW or
                                     t[f + 2] == ar.AIN or t[f + 2] == ar.HAH or t[f + 2] == ar.HEH or t[
                                         f + 2] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[f - 1:f + 3])
                ss = t[f - 1:f + 3]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
            if (f + 4 < len(t)) and (t[f + 1] == ar.ALEF) and (t[f + 2] == ' ') and (
                    t[f + 3] == ar.GHAIN or t[f + 3] == ar.ALEF_HAMZA_BELOW or t[f + 3] == ar.ALEF or t[
                f + 3] == ar.HAMZA or t[f + 3] == ar.ALEF_HAMZA_ABOVE or t[f + 3] == ar.AIN or t[f + 3] == ar.HAH or t[
                        f + 3] == ar.HEH or t[f + 3] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[f - 1:f + 4])
                ss = t[f - 1:f + 4]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
        for k in k1:
            if (k + 3 < len(t)) and (
                    t[k + 2] == ar.ALEF_HAMZA_BELOW or t[k + 2] == ar.GHAIN or t[k + 2] == ar.HAMZA or t[
                k + 2] == ar.ALEF or t[k + 2] == ar.ALEF_HAMZA_ABOVE or t[k + 2] == ar.AIN or t[k + 2] == ar.HAH or t[
                        k + 2] == ar.HEH or t[k + 2] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[k - 1:k + 3])
                ss = t[k - 1:k + 3]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')
            if (k + 4 < len(t)) and (t[k + 1] == ar.ALEF) and (t[k + 2] == ' ') and (
                    t[k + 2] == ar.GHAIN or t[k + 2] == ar.ALEF_HAMZA_BELOW or t[k + 2] == ar.ALEF or t[
                k + 2] == ar.HAMZA or t[k + 2] == ar.ALEF_HAMZA_ABOVE or t[k + 2] == ar.AIN or t[k + 2] == ar.HAH or t[
                        k + 2] == ar.HEH or t[k + 2] == ar.KHAH):
                self.declare(Ezhar(a='True'))
                print(t[k - 1:k + 4])
                ss = t[k - 1:k + 4]
                result.append("الحكم الحكم اظهار " + '(' + ss + ')')

    @Rule()
    def findEzharSHafawi(self):
        n1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
        for n in n1:
            if ar.is_sukun(t[n + 1]):
                if (n + 3 < len(t)) and (t[n + 2] == ar.YEH or t[n + 2] == ar.REH or t[n + 2] == ar.MEEM or t[
                    n + 2] == ar.LAM or t[n + 2] == ar.WAW or t[
                                             n + 2] == ar.NOON):
                    self.declare(EzharHalqi(a='True'))
                    print(t[n - 1:n + 3])
                    ss=t[n - 1:n + 3]
                    result.append("الحكم إظهار مطلق "+'('+ss+')')

            elif (n + 2 < len(t)) and (t[n + 1] == ar.YEH or t[n + 1] == ar.REH or t[n + 1] == ar.MEEM or t[
                n + 1] == ar.LAM or t[n + 1] == ar.WAW or t[
                                           n + 1] == ar.NOON):
                self.declare(EzharHalqi(a='True'))
                print(t[n - 1:n + 2])
                ss = t[n - 1:n + 2]
                result.append("الحكم إظهار مطلق " + '(' + ss + ')')

    @Rule()
    def findMaddEwad(self):
        f1 = []
        for i, char in enumerate(t):
            if char == ar.FATHATAN:
                f1.append(i)
        for f in f1:
            if f + 1 < len(t) and (t[f + 1] == ar.ALEF) and (f + 1 == len(t) - 1):
                self.declare(MaddEwad(a='True'))
                print(t[f - 1:f + 1])
                ss=t[f - 1:f + 1]
                result.append("الحكم مد عوض "+'('+ss+')')
            if f + 1 < len(t) and (t[f - 1] == ar.HAMZA) and (f + 1 == len(t) - 1):
                self.declare(MaddEwad(a='True'))
                print(t[f - 1:f + 1])
                ss=t[f - 1:f + 1]
                result.append("الحكم مد عوض "+'('+ss+')')

    @Rule()
    def findmadtmken(self):
        f1 = []
        d1 = []
        for i, char in enumerate(t):
            if char == ar.YEH:
                f1.append(i)
            if char == ar.WAW:
                d1.append(i)
        for f in f1:
            if f + 2 < len(t) and (t[f + 2] == ar.YEH) and (ar.is_haraka(t[f + 1])):
                self.declare(madtmken(a='True'))
                print(t[f - 1:f + 2])
                ss=t[f - 1:f + 2]
                result.append("الحكم مد تمكين "+'('+ss+')')
        for d in d1:
            if d + 2 < len(t) and (t[d + 2] == ar.WAW) and (ar.is_haraka(t[d + 1])):
                self.declare(madtmken(a='True'))
                print(t[d - 1:d + 2])
                ss = t[d - 1:d + 2]
                result.append("الحكم مد تمكين " + '(' + ss + ')')

    @Rule()
    def findMadd(self):
        n1 = []
        d1 = []
        f1 = []
        for i, char in enumerate(t):
            if char == ar.WAW:
                n1.append(i)
            if char == ar.ALEF:
                d1.append(i)
            if char == ar.YEH:
                f1.append(i)
        for l in n1:
            if l + 2 < len(t) and (ar.is_sukun(t[l + 1]) and t[l - 1] == ar.DAMMA) and (
                    not (ar.is_hamza(t[l + 2])) and not (ar.is_sukun(t[l + 2]))) and (not (l + 2 == len(t) - 1)):
                self.declare(Madd(a='true'))
                print(t[l - 1:l + 2])
                ss=t[l - 1:l + 2]
                result.append("الحكم مد طبيعي "+'('+ss+')')
            if l + 2 < len(t) and (ar.is_sukun(t[l + 1]) and t[l - 1] == ar.DAMMA) and (
                    not (ar.is_hamza(t[l + 2])) and not (ar.is_sukun(t[l + 2]))) and (l + 2 == len(t) - 1):
                self.declare(MaddAredLilsukun(a='true'))
                print(t[l - 1:l + 2])
                ss=t[l - 1:l + 2]
                result.append("الحكم مد عارض للسكون "+'('+ss+')')
            if l + 2 < len(t) and (not ar.is_shadda(t[l + 1])) and (not ar.is_haraka(t[l + 1])) and (
                    t[l - 1] == ar.DAMMA) and (
                    not (ar.is_hamza(t[l + 2])) and not (ar.is_sukun(t[l + 2]))) and (not (l + 2 == len(t) - 1)):
                self.declare(Madd(a='True'))
                print(t[l - 1:l + 2])
                ss=t[l - 1:l + 2]
                result.append("الحكم مد طبيعي "+'('+ss+')')
            if l + 2 < len(t) and (not ar.is_shadda(t[l + 1])) and (not ar.is_haraka(t[l + 1])) and (
                    t[l - 1] == ar.DAMMA) and (
                    not (ar.is_hamza(t[l + 2])) and not (ar.is_sukun(t[l + 2]))) and (l + 2 == len(t) - 1):
                self.declare(MaddAredLilsukun(a='True'))
                print(t[l - 1:l + 2])
                ss=t[l - 1:l + 2]
                result.append("الحكم مد عارض للسكون "+'('+ss+')')
            if l + 2 < len(t) and (ar.is_sukun(t[l + 1]) and ar.is_hamza(t[l - 2])) and t[l - 1] == ar.DAMMA:
                self.declare(MaddBadal(a='True'))
                print(t[l - 1:l + 2])
                ss=t[l - 1:l + 2]
                result.append("الحكم مد بدل "+'('+ss+')')
        for m in d1:
            if m + 1 < len(t) and (t[m - 1] == ar.FATHA) and (not ar.is_hamza(t[m + 1])) and (
                    not ar.is_sukun(t[m + 1])):
                self.declare(Madd(a='True'))
                print(t[m - 1:m + 1])
                ss=t[m - 1:m + 1]
                result.append("الحكم مد طبيعي "+'('+ss+')')
            if m + 1 < len(t) and (ar.is_hamza(t[m - 2])) and t[m - 1] == ar.FATHA:
                self.declare(MaddBadal(a='True'))
                print(t[m - 1:m + 1])
                ss = t[m - 1:m + 1]
                result.append("الحكم مد بدل " + '(' + ss + ')')
        for o in f1:
            if o + 2 < len(t) and (ar.is_sukun(t[o + 1]) and t[o - 1] == ar.KASRA) and (
                    not (ar.is_hamza(t[o + 2])) and (not (ar.is_sukun(t[o + 2])))) and (not (o + 2 == len(t) - 1)):
                self.declare(Madd(a='true'))
                print(t[o - 1:o + 2])
                ss = t[o - 1:o + 2]
                result.append("الحكم مد طبيعي " + '(' + ss + ')')
            if o + 2 < len(t) and (ar.is_sukun(t[o + 1]) and t[o - 1] == ar.KASRA) and (
                    not (ar.is_hamza(t[o + 2])) and (not (ar.is_sukun(t[o + 2])))) and (o + 2 == len(t) - 1):
                self.declare(MaddAredLilsukun(a='true'))
                print(t[o - 1:o + 2])
                ss = t[o - 1:o + 2]
                result.append("الحكم مد عارض للسكون " + '(' + ss + ')')
            if o + 2 < len(t) and (not ar.is_shadda(t[o + 1])) and (not ar.is_haraka(t[o + 1])) and (
                    t[o - 1] == ar.KASRA) and (
                    not (ar.is_hamza(t[o + 2])) and not (ar.is_sukun(t[o + 2]))) and (not (o + 2 == len(t) - 1)):
                self.declare(Madd(a='True'))
                print(t[o - 1:o + 2])
                ss = t[o - 1:o + 2]
                result.append("الحكم مد طبيعي " + '(' + ss + ')')
            if o + 2 < len(t) and (not ar.is_shadda(t[o + 1])) and (not ar.is_haraka(t[o + 1])) and (
                    t[o - 1] == ar.KASRA) and (
                    not (ar.is_hamza(t[o + 2])) and not (ar.is_sukun(t[o + 2]))) and (o + 2 == len(t) - 1):
                self.declare(MaddAredLilsukun(a='True'))
                print(t[o - 1:o + 2])
                ss = t[o - 1:o + 2]
                result.append("الحكم مد عارض للسكون " + '(' + ss + ')')
            if o + 1 < len(t) and (ar.is_sukun(t[o + 1]) and ar.is_hamza(t[o - 2])) and t[o - 1] == ar.KASRA:
                self.declare(MaddBadal(a='True'))
                print(t[o - 1:o + 1])
                ss = t[o - 1:o + 2]
                result.append("الحكم مد بدل " + '(' + ss + ')')


    @Rule()
    def findIqlab(self):
        n1 = []
        d1 = []
        f1 = []
        k1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
            if char == ar.DAMMATAN:
                d1.append(i)
            if char == ar.FATHATAN:
                f1.append(i)
            if char == ar.KASRATAN:
                k1.append(i)
        for n in n1:
            if (n + 4 < len(t)) and ar.is_sukun(t[n + 1]) and (t[n + 2] == ' '):
                if t[n + 3] == ar.BEH:
                    self.declare(Iqlab(a='True'))
                    print(t[n - 1: n + 4])
                    ss = t[n - 1: n + 4]
                    result.append("الحكم اقلاب " + '(' + ss + ')')

            elif (n + 3 < len(t)) and (t[n + 1] == ' '):
                if t[n + 2] == ar.BEH:
                    self.declare(Iqlab(a='True'))
                    print(t[n - 1: n + 3])
                    ss = t[n - 1: n + 3]
                    result.append("الحكم اقلاب " + '(' + ss + ')')

            elif (n + 3 < len(t)) and t[n + 1] == ar.BEH:
                self.declare(Iqlab(a='True'))
                print(t[n - 1: n + 3])
                ss = t[n - 1: n + 3]
                result.append("الحكم اقلاب " + '(' + ss + ')')

        for d in d1:
            if (d + 3 < len(t)) and t[d + 2] == ar.BEH:
                self.declare(Iqlab(a='True'))
                print(t[d - 1: d + 3])
                ss = t[d - 1: d + 3]
                result.append("الحكم اقلاب " + '(' + ss + ')')

            if (d + 4 < len(t)) and (t[d + 1] == ar.ALEF) and (t[d + 2] == ' ') and (t[d + 3] == ar.BEH):
                self.declare(Iqlab(a='True'))
                print(t[d - 1: d + 4])
                ss = t[d - 1: d + 4]
                result.append("الحكم اقلاب " + '(' + ss + ')')

        for f in f1:
            if (f + 3 < len(t)) and t[f + 2] == ar.BEH:
                self.declare(Iqlab(a='True'))
                print(t[f - 1: f + 3])
                ss = t[f - 1: f + 3]
                result.append("الحكم اقلاب " + '(' + ss + ')')

            if (f + 4 < len(t)) and (t[f + 1] == ar.ALEF) and (t[f + 2] == ' ') and (t[f + 3] == ar.BEH):
                self.declare(Iqlab(a='True'))
                print(t[f - 1: f + 4])
                ss = t[f - 1: f + 4]
                result.append("الحكم اقلاب " + '(' + ss + ')')

        for k in k1:
            if (k + 3 < len(t)) and (t[k + 2] == ar.BEH):
                self.declare(Iqlab(a='True'))
                print(t[k - 1: k + 3])
                ss = t[k - 1: k + 3]
                result.append("الحكم اقلاب " + '(' + ss + ')')

            if (k + 4 < len(t)) and (t[k + 1] == ar.ALEF) and (t[k + 2] == ' ') and (t[k + 3] == ar.BEH):
                self.declare(Iqlab(a='True'))
                print(t[k - 1: k + 4])
                ss = t[k - 1: k + 4]
                result.append("الحكم اقلاب " + '(' + ss + ')')

    @Rule()
    def findIdghaamWithGhunnah(self):
        n1 = []
        d1 = []
        f1 = []
        k1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
            if char == ar.DAMMATAN:
                d1.append(i)
            if char == ar.FATHATAN:
                f1.append(i)
            if char == ar.KASRATAN:
                k1.append(i)
        for n in n1:
            if (n + 4 < len(t)) and ar.is_sukun(t[n + 1]) and (t[n + 2] == ' '):
                if (t[n + 3] == ar.YEH) or (t[n + 3] == ar.NOON) or (t[n + 3] == ar.MEEM) or (t[n + 3] == ar.WAW):
                    self.declare(IdghaamWithGhunnah(a='True'))
                    print(t[n - 1: n + 4])
                    ss = t[n - 1: n + 4]
                    result.append("الحكم إدغام بغنة " + '(' + ss + ')')

            if (n + 3 < len(t)) and (t[n + 1] == ' '):
                if (t[n + 2] == ar.YEH) or (t[n + 2] == ar.NOON) or (t[n + 2] == ar.MEEM) or (t[n + 2] == ar.WAW):
                    self.declare(IdghaamWithGhunnah(a='True'))
                    print(t[n - 1: n + 3])
                    ss = t[n - 1: n + 3]
                    result.append("الحكم إدغام بغنة " + '(' + ss + ')')
        for d in d1:
            if (d + 3 < len(t)) and (
                    (t[d + 2] == ar.YEH) or (t[d + 2] == ar.NOON) or (t[d + 2] == ar.MEEM) or (t[d + 2] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[d - 1: d + 3])
                ss = t[d - 1: d + 3]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')

            if (d + 4 < len(t)) and (t[d + 1] == ar.ALEF) and (t[d + 2] == ' ') and (
                    (t[d + 3] == ar.YEH) or (t[d + 3] == ar.NOON) or (t[d + 3] == ar.MEEM) or (t[d + 3] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[d - 1: d + 4])
                ss = t[d - 1: d + 4]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')

        for f in f1:
            if (f + 3 < len(t)) and (
                    (t[f + 2] == ar.YEH) or (t[f + 2] == ar.NOON) or (t[f + 2] == ar.MEEM) or (t[f + 2] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[f - 1: f + 3])
                ss = t[f - 1: f + 4]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')

            if (f + 4 < len(t)) and (t[f + 1] == ar.ALEF) and (t[f + 2] == ' ') and (
                    (t[f + 3] == ar.YEH) or (t[f + 3] == ar.NOON) or (t[f + 3] == ar.MEEM) or (t[f + 3] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[f - 1: f + 4])
                ss = t[f - 1: f + 4]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')

        for k in k1:
            if (k + 3 < len(t)) and (
                    (t[k + 2] == ar.YEH) or (t[k + 2] == ar.NOON) or (t[k + 2] == ar.MEEM) or (t[k + 2] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[k - 1:k + 3])
                ss = t[k - 1: k + 3]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')
            if (k + 4 < len(t)) and (t[k + 1] == ar.ALEF) and (t[k + 2] == ' ') and (
                    (t[k + 3] == ar.YEH) or (t[k + 3] == ar.NOON) or (t[k + 3] == ar.MEEM) or (t[k + 3] == ar.WAW)):
                self.declare(IdghaamWithGhunnah(a='True'))
                print(t[k - 1:k + 4])
                ss = t[k - 1: k + 4]
                result.append("الحكم إدغام بغنة " + '(' + ss + ')')

    @Rule()
    def findIdghaamWithOutGhunnah(self):
        n1 = []
        d1 = []
        f1 = []
        k1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
            if char == ar.DAMMATAN:
                d1.append(i)
            if char == ar.FATHATAN:
                f1.append(i)
            if char == ar.KASRATAN:
                k1.append(i)

        for n in n1:
            if (n + 4 < len(t)) and ar.is_sukun(t[n + 1]) and (t[n + 2] == ' '):
                if (t[n + 3] == ar.LAM) or (t[n + 3] == ar.REH):
                    self.declare(IdghaamWithOutGhunnah(a='True'))
                    print(t[n - 1: n + 4])
                    ss = t[n - 1: n + 4]
                    result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
            elif (n + 3 < len(t)) and (t[n + 1] == ' '):
                if (t[n + 2] == ar.LAM) or (t[n + 2] == ar.REH):
                    self.declare(IdghaamWithOutGhunnah(a='True'))
                    print(t[n - 1: n + 3])
                    ss = t[n - 1: n + 3]
                    result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
        for d in d1:
            if (d + 3 < len(t)) and ((t[d + 2] == ar.LAM) or (t[d + 2] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[d - 1: d + 3])
                ss = t[d - 1: d + 3]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
            if (d + 4 < len(t)) and (t[d + 1] == ar.ALEF) and (t[d + 2] == ' ') and (
                    (t[d + 3] == ar.LAM) or (t[d + 3] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[d - 1: d + 4])
                ss = t[d - 1: d + 4]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
        for f in f1:
            if (f + 3 < len(t)) and ((t[f + 2] == ar.LAM) or (t[f + 2] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[f - 1: f + 3])
                ss = t[f - 1: f + 3]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
            if (f + 4 < len(t)) and (t[f + 1] == ar.ALEF) and (t[f + 2] == ' ') and (
                    (t[f + 3] == ar.LAM) or (t[f + 3] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[f - 1: f + 4])
                ss = t[f - 1: f + 4]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
        for k in k1:
            if (k + 3 < len(t)) and ((t[k + 2] == ar.LAM) or (t[k + 2] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[k - 1: k + 3])
                ss = t[k - 1: k + 3]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')
            if (k + 4 < len(t)) and (t[k + 1] == ar.ALEF) and (t[k + 2] == ' ') and (
                    (t[k + 3] == ar.LAM) or (t[k + 3] == ar.REH)):
                self.declare(IdghaamWithOutGhunnah(a='True'))
                print(t[k - 1: k + 4])
                ss = t[k - 1: k + 4]
                result.append("الحكم إدغام بلا غنة" + '(' + ss + ')')

    @Rule()
    def findIkhfa(self, ):
        n1 = []
        d1 = []
        f1 = []
        k1 = []
        for i, char in enumerate(t):
            if char == ar.NOON:
                n1.append(i)
            if char == ar.DAMMATAN:
                d1.append(i)
            if char == ar.FATHATAN:
                f1.append(i)
            if char == ar.KASRATAN:
                k1.append(i)
        for n in n1:
            if (n + 4 < len(t)) and ar.is_sukun(t[n + 1]):
                if (t[n + 2] == ' ') and (t[n + 3] == ar.SAD) or (t[n + 3] == ar.THAL) or (t[n + 3] == ar.THEH) or (
                        t[n + 3] == ar.KAF) or (t[n + 3] == ar.JEEM) or (t[n + 3] == ar.SHEEN) or (
                        t[n + 3] == ar.QAF) or (t[n + 3] == ar.SEEN) or (t[n + 3] == ar.DAL) or (
                        t[n + 3] == ar.TAH) or (t[n + 3] == ar.ZAIN) or (t[n + 3] == ar.TEH) or (
                        t[n + 3] == ar.DAD) or (t[n + 3] == ar.ZAH) or (t[n + 3] == ar.FEH):
                    self.declare(Ikhfa(a='True'))
                    print(t[n - 1: n + 4])
                    ss = t[n - 1: n + 4]
                    result.append("الحكم إخفاء" + '(' + ss + ')')
                elif (t[n + 2] == ar.SAD) or (t[n + 2] == ar.THAL) or (t[n + 2] == ar.THEH) or (t[n + 2] == ar.KAF) or (
                        t[n + 2] == ar.JEEM) or (t[n + 2] == ar.SHEEN) or (t[n + 2] == ar.QAF) or (
                        t[n + 2] == ar.SEEN) or (t[n + 2] == ar.DAL) or (t[n + 2] == ar.TAH) or (
                        t[n + 2] == ar.ZAIN) or (t[n + 2] == ar.TEH) or (t[n + 2] == ar.DAD) or (
                        t[n + 2] == ar.ZAH) or (t[n + 2] == ar.FEH):
                    self.declare(Ikhfa(a='True'))
                    print(t[n - 1: n + 3])
                    ss = t[n - 1: n + 3]
                    result.append("الحكم إخفاء" + '(' + ss + ')')
            if (n + 3 < len(t)) and t[n + 1] == ' ':
                if (t[n + 2] == ar.SAD) or (t[n + 2] == ar.THAL) or (t[n + 2] == ar.THEH) or (t[n + 2] == ar.KAF) or (
                        t[n + 2] == ar.JEEM) or (t[n + 2] == ar.SHEEN) or (t[n + 2] == ar.QAF) or (
                        t[n + 2] == ar.SEEN) or (t[n + 2] == ar.DAL) or (t[n + 2] == ar.TAH) or (
                        t[n + 2] == ar.ZAIN) or (t[n + 2] == ar.TEH) or (t[n + 2] == ar.DAD) or (
                        t[n + 2] == ar.ZAH) or (t[n + 2] == ar.FEH):
                    self.declare(Ikhfa(a='True'))
                    print(t[n - 1: n + 3])
                    ss = t[n - 1: n + 3]
                    result.append("الحكم إخفاء" + '(' + ss + ')')
        for d in d1:
            if (d + 3 < len(t)) and (
                    (t[d + 2] == ar.SAD) or (t[d + 2] == ar.THAL) or (t[d + 2] == ar.THEH) or (t[d + 2] == ar.KAF) or (
                    t[d + 2] == ar.JEEM) or (t[d + 2] == ar.SHEEN) or (t[d + 2] == ar.QAF) or (t[d + 2] == ar.SEEN) or (
                            t[d + 2] == ar.DAL) or (t[d + 2] == ar.TAH) or (t[d + 2] == ar.ZAIN) or (
                            t[d + 2] == ar.TEH) or (t[d + 2] == ar.DAD) or (t[d + 2] == ar.ZAH) or (
                            t[d + 2] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[d - 1: d + 3])
                ss = t[d - 1: d + 3]
                result.append("الحكم إخفاء" + '(' + ss + ')')
            if (d + 4 < len(t)) and (t[d + 1] == ar.ALEF) and (t[d + 2] == ' ') and (
                    (t[d + 3] == ar.SAD) or (t[d + 3] == ar.THAL) or (t[d + 3] == ar.THEH) or (t[d + 3] == ar.KAF) or (
                    t[d + 3] == ar.JEEM) or (t[d + 3] == ar.SHEEN) or (t[d + 3] == ar.QAF) or (t[d + 3] == ar.SEEN) or (
                            t[d + 3] == ar.DAL) or (t[d + 3] == ar.TAH) or (t[d + 3] == ar.ZAIN) or (
                            t[d + 3] == ar.TEH) or (t[d + 3] == ar.DAD) or (t[d + 3] == ar.ZAH) or (
                            t[d + 3] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[d - 1: d + 4])
                ss = t[d - 1: d + 4]
                result.append("الحكم إخفاء" + '(' + ss + ')')
        for f in f1:
            if (f + 3 < len(t)) and (
                    (t[f + 2] == ar.SAD) or (t[f + 2] == ar.THAL) or (t[f + 2] == ar.THEH) or (t[f + 2] == ar.KAF) or (
                    t[f + 2] == ar.JEEM) or (t[f + 2] == ar.SHEEN) or (t[f + 2] == ar.QAF) or (t[f + 2] == ar.SEEN) or (
                            t[f + 2] == ar.DAL) or (t[f + 2] == ar.TAH) or (t[f + 2] == ar.ZAIN) or (
                            t[f + 2] == ar.TEH) or (t[f + 2] == ar.DAD) or (t[f + 2] == ar.ZAH) or (
                            t[f + 2] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[f - 1: f + 3])
                ss = t[f - 1: f + 3]
                result.append("الحكم إخفاء" + '(' + ss + ')')
            if (f + 4 < len(t)) and (t[f + 1] == ar.ALEF) and (t[f + 2] == ' ') and (
                    (t[f + 3] == ar.SAD) or (t[f + 3] == ar.THAL) or (t[f + 3] == ar.THEH) or (t[f + 3] == ar.KAF) or (
                    t[f + 3] == ar.JEEM) or (t[f + 3] == ar.SHEEN) or (t[f + 3] == ar.QAF) or (t[f + 3] == ar.SEEN) or (
                            t[f + 3] == ar.DAL) or (t[f + 3] == ar.TAH) or (t[f + 3] == ar.ZAIN) or (
                            t[f + 3] == ar.TEH) or (t[f + 3] == ar.DAD) or (t[f + 3] == ar.ZAH) or (
                            t[f + 3] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[f - 1: f + 4])
                ss = t[f - 1: f + 4]
                result.append("الحكم إخفاء" + '(' + ss + ')')
        for k in k1:
            if (k + 3 < len(t)) and (
                    (t[k + 2] == ar.SAD) or (t[k + 2] == ar.THAL) or (t[k + 2] == ar.THEH) or (t[k + 2] == ar.KAF) or (
                    t[k + 2] == ar.JEEM) or (t[k + 2] == ar.SHEEN) or (t[k + 2] == ar.QAF) or (t[k + 2] == ar.SEEN) or (
                            t[k + 2] == ar.DAL) or (t[k + 2] == ar.TAH) or (t[k + 2] == ar.ZAIN) or (
                            t[k + 2] == ar.TEH) or (t[k + 2] == ar.DAD) or (t[k + 2] == ar.ZAH) or (
                            t[k + 2] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[k - 1: k + 3])
                ss = t[k - 1: k + 3]
                result.append("الحكم إخفاء" + '(' + ss + ')')
            if (k + 4 < len(t)) and (t[k + 1] == ar.ALEF) and (t[k + 2] == ' ') and (
                    (t[k + 3] == ar.SAD) or (t[k + 3] == ar.THAL) or (t[k + 3] == ar.THEH) or (t[k + 3] == ar.KAF) or (
                    t[k + 3] == ar.JEEM) or (t[k + 3] == ar.SHEEN) or (t[k + 3] == ar.QAF) or (t[k + 3] == ar.SEEN) or (
                            t[k + 3] == ar.DAL) or (t[k + 3] == ar.TAH) or (t[k + 3] == ar.ZAIN) or (
                            t[k + 3] == ar.TEH) or (t[k + 3] == ar.DAD) or (t[k + 3] == ar.ZAH) or (
                            t[k + 3] == ar.FEH)):
                self.declare(Ikhfa(a='True'))
                print(t[k - 1: k + 4])
                ss = t[k - 1: k + 4]
                result.append("الحكم إخفاء" + '(' + ss + ')')

    @Rule()
    def findQalqalahSughraa(self):
        q1 = []
        tah1 = []
        b1 = []
        j1 = []
        d1 = []
        for i, char in enumerate(t):
            if char == ar.QAF:
                q1.append(i)
            if char == ar.TAH:
                tah1.append(i)
            if char == ar.BEH:
                b1.append(i)
            if char == ar.JEEM:
                j1.append(i)
            if char == ar.DAL:
                d1.append(i)
        for q in q1:
            # if (q != -1) and (q+1 < len(t)):
            if ar.is_sukun(t[q + 1]) and (q + 2 < len(t)):
                self.declare(QalqalahSughraa(a='True'))
                print(t[q - 1: q + 2])
                ss = t[q - 1: q + 2]
                result.append("الحكم قلقلة صغرى " + '(' + ss + ')')
        for tah in tah1:
            # if tah != -1 and tah+1 < len(t):
            if ar.is_sukun(t[tah + 1]) and tah + 2 < len(t):
                self.declare(QalqalahSughraa(a='True'))
                print(t[tah - 1: tah + 2])
                ss = t[tah - 1: tah + 2]
                result.append("الحكم قلقلة صغرى " + '(' + ss + ')')
        for b in b1:
            # if b != -1 and b+1 < len(t):
            if ar.is_sukun(t[b + 1]) and b + 2 < len(t):
                self.declare(QalqalahSughraa(a='True'))
                print(t[b - 1: b + 2])
                ss = t[b - 1: b + 2]
                result.append("الحكم قلقلة صغرى " + '(' + ss + ')')
        for j in j1:
            # if j != -1 and j+1 < len(t):
            if ar.is_sukun(t[j + 1]) and j + 2 < len(t):
                self.declare(QalqalahSughraa(a='True'))
                print(t[j - 1: j + 2])
                ss = t[j - 1: j + 2]
                result.append("الحكم قلقلة صغرى " + '(' + ss + ')')
        for d in d1:
            # if d != -1 and d+1 < len(t):
            if ar.is_sukun(t[d + 1]) and d + 2 < len(t):
                self.declare(QalqalahSughraa(a='True'))
                print(t[d - 1: d + 2])
                ss = t[d - 1: d + 2]
                result.append("الحكم قلقلة صغرى " + '(' + ss + ')')

    @Rule()
    def findQalqalahKubraa(self):
        q1 = []
        tah1 = []
        b1 = []
        j1 = []
        d1 = []
        for i, char in enumerate(t):
            if char == ar.QAF:
                q1.append(i)
            if char == ar.TAH:
                tah1.append(i)
            if char == ar.BEH:
                b1.append(i)
            if char == ar.JEEM:
                j1.append(i)
            if char == ar.DAL:
                d1.append(i)
        for q in q1:
            # if (q != -1) and (q + 1 < len(t)):
            if ar.is_sukun(t[q + 1]) and (q + 2 == len(t) - 1):
                self.declare(QalqalahKubraa(a='True'))
                print(t[q - 1: q + 2])
                ss = t[q - 1: q + 2]
                result.append("الحكم قلقلة كبرى" + '(' + ss + ')')
        for tah in tah1:
            # if tah != -1 and tah + 1 < len(t):
            if ar.is_sukun(t[tah + 1]) and (tah + 2 == len(t) - 1):
                self.declare(QalqalahKubraa(a='True'))
                print(t[tah - 1: tah + 2])
                ss = t[tah - 1: tah + 2]
                result.append("الحكم قلقلة كبرى" + '(' + ss + ')')
        for b in b1:
            # if b != -1 and b + 1 < len(t):
            if ar.is_sukun(t[b + 1]) and (b + 2 == len(t) - 1):
                self.declare(QalqalahKubraa(a='True'))
                print(t[b - 1: b + 2])
                ss = t[b - 1: b + 2]
                result.append("الحكم قلقلة كبرى" + '(' + ss + ')')
        for j in j1:
            # if j != -1 and j + 1 < len(t):
            if ar.is_sukun(t[j + 1]) and (j + 2 == len(t) - 1):
                self.declare(QalqalahKubraa(a='True'))
                print(t[j - 1: j + 2])
                ss = t[j - 1: j + 2]
                result.append("الحكم قلقلة كبرى" + '(' + ss + ')')
        for d in d1:
            # if d != -1 and d + 1 < len(t):
            if ar.is_sukun(t[d + 1]) and (d + 2 == len(t) - 1):
                self.declare(QalqalahKubraa(a='True'))
                print(t[d - 1: d + 2])
                ss = t[d - 1: d + 2]
                result.append("الحكم قلقلة كبرى" + '(' + ss + ')')

    @Rule()
    def findLafzGlalahMuraqaq(self):
        lafzglalah = t.find('اللَّه')
        if lafzglalah != -1:
            if t[lafzglalah - 2] == "ِ" or t[lafzglalah - 2] == "ٍ":
                self.declare(LafzGlalahMuraqaq(a='True'))
                print(t[lafzglalah - 2: lafzglalah + 7])
                ss = t[lafzglalah - 2: lafzglalah + 7]
                result.append("الحكم لفظ جلالة مرقق" + '(' + ss + ')')
            if t[lafzglalah - 2] == 'ْ' and (t[lafzglalah - 4] == "ِ" or t[lafzglalah - 4] == "ٍ"):
                self.declare(LafzGlalahMuraqaq(a='True'))
                print(t[lafzglalah - 2: lafzglalah + 7])
                ss = t[lafzglalah - 2: lafzglalah + 7]
                result.append("الحكم لفظ جلالة مرقق" + '(' + ss + ')')

    @Rule()
    def findLafzGlalahMufakham(self):
        lafzglalah = t.find('اللَّه')
        if lafzglalah != -1:
            if t[lafzglalah - 2] == 'َ' or t[lafzglalah - 2] == 'ً' or t[lafzglalah - 2] == 'ُ' or t[
                lafzglalah - 2] == 'ٌ':
                self.declare(LafzGlalahMufakham(a='True'))
                print(t[lafzglalah - 2: lafzglalah + 7])
                ss = t[lafzglalah - 2: lafzglalah + 7]
                result.append("الحكم لفظ جلالة مفخم" + '(' + ss + ')')
            if t[lafzglalah - 2] == 'ْ' and (
                    t[lafzglalah - 4] == 'َ' or t[lafzglalah - 4] == 'ً' or t[lafzglalah - 4] == 'ُ' or t[
                lafzglalah - 4] == 'ٌ'):
                self.declare(LafzGlalahMufakham(a='True'))
                print(t[lafzglalah - 2: lafzglalah + 7])
                ss = t[lafzglalah - 2: lafzglalah + 7]
                result.append("الحكم لفظ جلالة مفخم" + '(' + ss + ')')

    @Rule()
    def findTfkemAlRaa(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.REH:
                r.append(i)
        for r1 in r:
            if (r1 + 2 < len(t)) and (t[r1 + 1] == ar.DAMMA or t[r1 + 2] == ar.DAMMA or t[r1 + 1] == ar.DAMMATAN or t[
                r1 + 2] == ar.DAMMATAN):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1: r1 + 2] + '1')
                ss=t[r1: r1 + 2]
                result.append("الحكم راء مفخمة "+'('+ss+')')
            elif r1 + 2 < len(t) and (t[r1 + 1] == ar.FATHA or t[r1 + 2] == ar.FATHA or (
                    t[r1 + 1] == ar.ALEF and t[r1 + 2] == ar.FATHATAN)):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1: r1 + 2] + '2')
                ss = t[r1: r1 + 2]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')
            elif (r1 + 1 < len(t)) and ar.is_sukun(t[r1 + 1]) and (t[r1 - 1] == ar.DAMMA):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1 - 1: r1 + 1] + '3')
                ss = t[r1-1: r1 + 1]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')
            elif (r1 + 1 < len(t)) and ar.is_sukun(t[r1 + 1]) and (t[r1 - 1] == ar.FATHA):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1 - 1: r1 + 1] + '4')
                ss = t[r1-1: r1 + 1]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')
            elif (r1 - 3 >= 0) & ar.is_sukun(t[r1 - 1]) and (
                    t[r1 - 3] == ar.FATHA or t[r1 - 3] == ar.DAMMA):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1 - 3: r1 + 2] + '5')
                ss = t[r1-3: r1 + 2]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')
            elif r1 - 4 >= 0 and ar.is_sukun(t[r1 + 1]) and (
                    (ar.is_sukun(t[r1 - 1]) and t[r1 - 2] == ar.ALEF and t[r1 - 3] == ' ' and t[
                        r1 - 4] == ar.KASRA) or (t[r1 - 1] == ar.ALEF and t[r1 - 2] == ' ' and t[
                r1 - 3] == ar.KASRA)):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1 - 4: r1 + 1] + ' 6')
                ss = t[r1-4: r1 + 1]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')
            elif (r1 + 2 < len(t)) and ar.is_sukun(t[r1 + 1]) and (t[r1 - 1] == ar.KASRA) and (
                    t[r1 + 2] == ar.KHAH or t[r1 + 2] == ar.SAD or t[r1 + 2] == ar.DAD or t[r1 + 2] == ar.GHAIN or t[
                r1 + 2] == ar.TAH or t[r1 + 2] == ar.QAF or t[r1 + 2] == ar.ZAH):
                self.declare(TfkemAlRaa(a='True'))
                print(t[r1 - 2:r1 + 2] + '7')
                ss = t[r1-2: r1 + 2]
                result.append("الحكم راء مفخمة " + '(' + ss + ')')

    @Rule()
    def findTarkekAlRaa(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.REH:
                r.append(i)
        for r1 in r:
            if (r1 + 1 < len(t)) and (t[r1 + 1] == ar.KASRA) and (not ar.is_sukun(t[r1 - 1])):
                self.declare(TarkekAlRaa(a='True'))
                print(t[r1 - 2: r1 + 2] + '1')
                ss=t[r1 - 2: r1 + 2]
                result.append('الحكم الراء مرققة'+'('+ss+')')
            elif (r1 + 1 < len(t)) and (ar.is_sukun(t[r1 + 1])) and (t[r1 - 1] == ar.KASRA):
                self.declare(TarkekAlRaa(a='True'))
                print(t[r1 - 2: r1 + 2] + '2')
                ss = t[r1 - 2: r1 + 2]
                result.append('الحكم الراء مرققة' + '(' + ss + ')')
            elif (r1 - 3 >= 0) and (ar.is_sukun(t[r1 - 1]) and (not t[r1 - 1] == ar.YEH)) and (t[r1 - 3] == ar.KASRA):
                self.declare(TarkekAlRaa(a='True'))
                print(t[r1 - 2: r1 + 2] + '3')
                ss = t[r1 - 2: r1 + 2]
                result.append('الحكم الراء مرققة' + '(' + ss + ')')
            elif (r1 - 2 >= 0) and ((ar.is_sukun(t[r1 - 1]) and t[r1 - 2] == ar.YEH) or t[r1 - 1] == ar.YEH):
                self.declare(TarkekAlRaa(a='True'))
                print(t[r1 - 2: r1 + 1] + '4')
                ss = t[r1 - 2: r1 + 1]
                result.append('الحكم الراء مرققة' + '(' + ss + ')')
            elif (r1 + 3 < len(t) and t[r1 + 2] == ' ' and ar.is_sukun(t[r1 + 1]) and (
                    t[r1 + 3] == ar.KHAH or t[r1 + 3] == ar.SAD or t[r1 + 3] == ar.DAD or t[r1 + 3] == ar.GHAIN or t[
                r1 + 3] == ar.TAH or t[r1 + 3] == ar.QAF or t[r1 + 3] == ar.ZAH)):
                self.declare(TarkekAlRaa(a='True'))
                print(t[r1: r1 + 3] + '5')
                ss = t[r1 : r1 + 3]
                result.append('الحكم الراء مرققة' + '(' + ss + ')')

    @Rule()
    def findTafkemAlEstalaa(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.KHAH or ar.SAD or ar.QAF or ar.GHAIN or ar.TAH or ar.ZAH:
                r.append(i)
        for r1 in r:
            if r1 + 2 < len(t) and r1 + 1 < len(t) and (
                    t[r1] == ar.KHAH or t[r1] == ar.SAD or t[r1] == ar.DAD or t[r1] == ar.GHAIN or t[r1] == ar.TAH or t[
                r1] == ar.QAF or t[r1] == ar.ZAH) and (r1 + 2 < len(t) and (t[r1 + 1] == ar.FATHA or t[r1 + 2] == ar.FATHA)):
                self.declare(TafkemAlEstalaa(a='True'))
                print(t[r1: r1 + 2] + '1')
                ss = t[r1: r1 + 2]
                result.append('الحكم تفخيم حرف استعلاء (خص ضغط قظ)'+'('+ss+')')
            elif r1 + 2 < len(t) and r1 + 1 < len(t) and (
                    t[r1] == ar.KHAH or t[r1] == ar.SAD or t[r1] == ar.DAD or t[r1] == ar.GHAIN or t[r1] == ar.TAH or t[
                r1] == ar.QAF or t[r1] == ar.ZAH) and (
                    (t[r1 + 1] == ar.FATHA or t[r1 + 2] == ar.FATHA) and (not t[r1 + 2] == ar.ALEF)):
                self.declare(TafkemAlEstalaa(a='True'))
                print(t[r1: r1 + 2] + '2')
                ss = t[r1: r1 + 2]
                result.append('الحكم تفخيم حرف استعلاء (خص ضغط قظ)' + '(' + ss + ')')
            elif (r1 + 1 < len(t)) and (
                    t[r1] == ar.KHAH or t[r1] == ar.SAD or t[r1] == ar.DAD or t[r1] == ar.GHAIN or t[r1] == ar.TAH or t[
                r1] == ar.QAF or t[r1] == ar.ZAH) and (t[r1 + 1] == ar.DAMMA or t[r1 + 2] == ar.DAMMA):
                self.declare(TafkemAlEstalaa(a='True'))
                print(t[r1: r1 + 1] + '3')
                ss = t[r1: r1 + 1]
                result.append('الحكم تفخيم حرف استعلاء (خص ضغط قظ)' + '(' + ss + ')')
            elif (r1 + 1 < len(t)) and (
                    t[r1] == ar.KHAH or t[r1] == ar.SAD or t[r1] == ar.DAD or t[r1] == ar.GHAIN or t[r1] == ar.TAH or t[
                r1] == ar.QAF or t[r1] == ar.ZAH) and (ar.is_sukun(t[r1 + 1])):
                self.declare(TafkemAlEstalaa(a='True'))
                print(t[r1: r1 + 1] + '4')
                ss = t[r1: r1 + 1]
                result.append('الحكم تفخيم حرف استعلاء (خص ضغط قظ)' + '(' + ss + ')')
            elif r1 + 2 < len(t) and r1 + 1 < len(t) and (
                    t[r1] == ar.KHAH or t[r1] == ar.SAD or t[r1] == ar.DAD or t[r1] == ar.GHAIN or t[r1] == ar.TAH or t[
                r1] == ar.QAF or t[r1] == ar.ZAH) and (t[r1 + 1] == ar.KASRA or t[r1 + 2] == ar.KASRA):
                self.declare(TafkemAlEstalaa(a='True'))
                print(t[r1: r1 + 3] + '5')
                ss = t[r1: r1 + 3]
                result.append('الحكم تفخيم حرف استعلاء (خص ضغط قظ)' + '(' + ss + ')')

    @Rule()
    def findTafkemAlAlef(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.ALEF:
                r.append(i)
        for r1 in r:
            if r1 - 2 < len(t) and (
                    t[r1 - 2] == ar.KHAH or t[r1 - 2] == ar.SAD or t[r1 - 2] == ar.DAD or t[r1 - 2] == ar.GHAIN or t[
                r1 - 2] == ar.TAH or t[r1 - 2] == ar.QAF or t[r1 - 2] == ar.ZAH):
                self.declare(TafkemAlAlef(a='True'))
                print(t[r1 - 2: r1 + 1])
                tt = t[r1 - 2: r1 + 1]
                result.append('الحكم : تفخيم الالف ' + '(' + tt + ')')

    @Rule()
    def findTarkekAlAlef(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.ALEF:
                r.append(i)
        for r1 in r:
            if r1 - 2 < len(t) and not (
                    t[r1 - 2] == ar.KHAH or t[r1 - 2] == ar.SAD or t[r1 - 2] == ar.DAD or t[r1 - 2] == ar.GHAIN or t[
                r1 - 2] == ar.TAH or t[r1 - 2] == ar.QAF or t[r1 - 2] == ar.ZAH) and not (t[r1 - 1] == ' ') and not (
                    ar.is_hamza(t[r1 - 1])):
                self.declare(TarkekAlAlef(a='True'))
                print(t[r1 - 2: r1 + 1])
                tt = t[r1 - 2: r1 + 1]
                result.append('الحكم : ترقيق الالف ' + '(' + tt + ')')

    @Rule()
    def findLamAlmarefa(self):
        r = []
        for i, char in enumerate(t):
            if char == ar.LAM:
                r.append(i)
        for r1 in r:
            if t[r1 - 1] == ar.ALEF and ((ar.is_sukun(t[r1 + 1]) and r1 + 2 < len(t) and (
                    t[r1 + 2] == ar.TAH or t[r1 + 2] == ar.THEH or t[r1 + 2] == ar.SAD or t[r1 + 2] == ar.REH or t[
                r1 + 2] == ar.TEH or t[r1 + 2] == ar.DAD or t[r1 + 2] == ar.THAL or t[r1 + 2] == ar.NOON or t[
                        r1 + 2] == ar.DAL or t[r1 + 2] == ar.SEEN or t[r1 + 2] == ar.ZAH or t[
                        r1 + 2] == ar.ZAIN or t[r1 + 2] == ar.SHEEN or t[r1 + 2] == ar.LAM)) or (
                                                 (not ar.is_sukun(t[r1 + 1])) and (
                                                 (r1 + 2 < len(t) and (
                                                         t[r1 + 2] == ar.ALEF_HAMZA_ABOVE or t[r1 + 2] == ar.ALEF or t[
                                                     r1 + 2] == ar.ALEF_HAMZA_BELOW)) or
                                                 t[r1 + 1] == ar.TAH or t[r1 + 1] == ar.THEH or t[r1 + 1] == ar.SAD or
                                                 t[
                                                     r1 + 1] == ar.REH or t[
                                                     r1 + 1] == ar.TEH or t[r1 + 1] == ar.DAD or t[r1 + 1] == ar.THAL or
                                                 t[r1 + 1] == ar.NOON or t[
                                                     r1 + 1] == ar.DAL or t[r1 + 1] == ar.SEEN or
                                                 t[r1 + 1] == ar.ZAH or t[
                                                     r1 + 1] == ar.ZAIN or t[r1 + 1] == ar.SHEEN or t[
                                                     r1 + 1] == ar.LAM)) or (t[r1 + 1] == ar.SHADDA and (
                    (r1 + 2 < len(t) and (t[r1 + 2] == ar.ALEF_HAMZA_ABOVE or t[r1 + 2] == ar.ALEF or t[
                        r1 + 2] == ar.ALEF_HAMZA_BELOW)) or
                    (r1 + 3 < len(t) and t[r1 + 3] == ar.TAH or t[r1 + 3] == ar.THEH or t[r1 + 3] == ar.SAD or
                     t[
                         r1 + 3] == ar.REH or t[
                         r1 + 3] == ar.TEH or t[r1 + 3] == ar.DAD or t[r1 + 3] == ar.THAL or
                     t[r1 + 3] == ar.NOON or t[
                         r1 + 3] == ar.DAL or t[r1 + 3] == ar.SEEN or
                     t[r1 + 3] == ar.ZAH or t[
                         r1 + 3] == ar.ZAIN or t[r1 + 3] == ar.SHEEN or t[
                         r1 + 3] == ar.LAM)))):
                self.declare(LamAlmarefa(a='True'))
                print(t[r1: r1 + 2] + "  لام شمسية ")
                tt = t[r1: r1 + 2]
                result.append('الحكم : لام شمسية ' + '(' + tt + ')')
            if t[r1 - 1] == ar.ALEF and ((ar.is_sukun(t[r1 + 1]) and r1 + 2 < len(t) and (
                    t[r1 + 2] == ar.ALEF_HAMZA_ABOVE or t[r1 + 2] == ar.ALEF or t[r1 + 2] == ar.ALEF_HAMZA_BELOW or t[
                r1 + 2] == ar.BEH or t[r1 + 2] == ar.GHAIN or t[r1 + 2] == ar.HAH or t[
                        r1 + 2] == ar.JEEM or t[r1 + 2] == ar.KAF or t[r1 + 2] == ar.WAW or t[r1 + 2] == ar.KHAH or t[
                        r1 + 2] == ar.FEH or t[r1 + 2] == ar.AIN or t[r1 + 2] == ar.QAF or t[r1 + 2] == ar.YEH or t[
                        r1 + 2] == ar.MEEM or t[r1 + 2] == ar.HEH)) or (
                                                 (not ar.is_sukun(t[r1 + 1])) and (
                                                 (r1 + 2 < len(t) and (
                                                         t[r1 + 2] == ar.ALEF_HAMZA_ABOVE or t[r1 + 2] == ar.ALEF or t[
                                                     r1 + 2] == ar.ALEF_HAMZA_BELOW)) or t[r1 + 1] == ar.BEH or t[
                                                     r1 + 1] == ar.GHAIN or t[r1 + 1] == ar.HAH or t[
                                                     r1 + 1] == ar.JEEM or t[r1 + 1] == ar.KAF or t[
                                                     r1 + 1] == ar.WAW or t[r1 + 1] == ar.KHAH or t[
                                                     r1 + 1] == ar.FEH or t[r1 + 1] == ar.AIN or t[
                                                     r1 + 1] == ar.QAF or t[r1 + 1] == ar.YEH or t[
                                                     r1 + 1] == ar.MEEM or t[r1 + 1] == ar.HEH)) or (
                                                 t[r1 + 1] == ar.SHADDA and (
                                                 (r1 + 2 < len(t) and (
                                                         t[r1 + 2] == ar.ALEF_HAMZA_ABOVE or t[r1 + 2] == ar.ALEF or t[
                                                     r1 + 2] == ar.ALEF_HAMZA_BELOW)) or (
                                                         r1 + 3 < len(t) and (t[r1 + 3] == ar.BEH or t[
                                                     r1 + 3] == ar.GHAIN or t[r1 + 3] == ar.HAH or t[
                                                                                  r1 + 3] == ar.JEEM or t[
                                                                                  r1 + 3] == ar.KAF or t[
                                                                                  r1 + 3] == ar.WAW or t[
                                                                                  r1 + 3] == ar.KHAH or t[
                                                                                  r1 + 3] == ar.FEH or t[
                                                                                  r1 + 3] == ar.AIN or t[
                                                                                  r1 + 3] == ar.QAF or t[
                                                                                  r1 + 3] == ar.YEH or t[
                                                                                  r1 + 3] == ar.MEEM or t[
                                                                                  r1 + 3] == ar.HEH))))):
                self.declare(LamAlmarefa(a='True'))
                print(t[r1: r1 + 2] + "  لام قمرية ")
                tt = t[r1: r1 + 2]
                result.append('الحكم : لام قمرية ' + '(' + tt + ')')

    @Rule()
    def findikhfaa_shafawi(self):
        t1 = ar.strip_shadda(t)
        m1 = []
        for i, char in enumerate(t1):
            if char == ar.MEEM:
                m1.append(i)
        for m in m1:
            if m + 1 < len(t1) and ar.is_sukun(t1[m + 1]):
                if m + 2 < len(t1) and t1[m + 2] == ' ':
                    if m + 3 < len(t1) and t1[m + 3] == ar.BEH:
                        self.declare(ikhfaa_shafawi(a='True'))
                        print(t1[m - 1: m + 5])
                        ss=t1[m - 1: m + 5]
                        result.append("الحكم اخفاء شفوي"+'('+ss+')')
            elif m + 1 < len(t1) and t1[m + 1] == ' ':
                if m + 2 < len(t1) and t1[m + 2] == ar.BEH:
                    self.declare(ikhfaa_shafawi(a='True'))
                    print(t1[m - 1: m + 5])
                    ss = t1[m - 1: m + 5]
                    result.append("الحكم اخفاء شفوي" + '(' + ss + ')')

    @Rule()
    def findidgam_shafawi(self):
        t1 = ar.strip_shadda(t)
        m1 = []
        for i, char in enumerate(t1):
            if char == ar.MEEM:
                m1.append(i)
        for m in m1:
            if m + 1 < len(t1) and ar.is_sukun(t1[m + 1]):
                if m + 2 < len(t1) and t1[m + 2] == ' ':
                    if m + 3 < len(t1) and m + 4 < len(t1) and t1[m + 3] == ar.MEEM and not (ar.is_sukun(t1[m + 4])):
                        self.declare(idgam_shafawi(a='True'))
                        print(t1[m - 1: m + 5])
                        ss=t1[m - 1: m + 5]
                        result.append("الحكم ادغام شفوي"+'('+ss+')')
            elif m + 1 < len(t1) and t1[m + 1] == ' ':
                if m + 2 < len(t1) and m + 3 < len(t1) and t1[m + 2] == ar.MEEM and not (ar.is_sukun(t1[m + 3])):
                    self.declare(idgam_shafawi(a='True'))
                    print(t1[m - 1: m + 5])
                    ss = t1[m - 1: m + 5]
                    result.append("الحكم ادغام شفوي" + '(' + ss + ')')

    @Rule()
    def findizhar_shafawi(self):
        t1 = ar.strip_shadda(t)
        m1 = []
        for i, char in enumerate(t1):
            if char == ar.MEEM:
                m1.append(i)
        for m in m1:
            if m + 1 < len(t1) and ar.is_sukun(t1[m + 1]):
                if m + 2 < len(t1) and t1[m + 2] == ' ':
                    if m + 3 < len(t1) and t1[m + 3] != ar.BEH and t1[m + 3] != ar.MEEM:
                        self.declare(izhar_shafawi(a='True'))
                        print(t1[m - 1: m + 5])
                        ss=t1[m - 1: m + 5]
                        result.append("الحكم اظهار شفوي"+'('+ss+')')
                elif m + 2 < len(t1) and t1[m + 2] != ar.BEH and t1[m + 2] != ar.MEEM:
                    self.declare(izhar_shafawi(a='True'))
                    print(t1[m - 1: m + 5])
                    ss = t1[m - 1: m + 5]
                    result.append("الحكم اظهار شفوي" + '(' + ss + ')')
            elif m + 1 < len(t1) and t1[m + 1] == ' ':
                if m + 2 < len(t1) and t1[m + 2] != ar.BEH and t1[m + 2] != ar.MEEM:
                    self.declare(izhar_shafawi(a='True'))
                    print(t1[m - 1: m + 5])
                    ss = t1[m - 1: m + 5]
                    result.append("الحكم اظهار شفوي" + '(' + ss + ')')
            elif m + 1 < len(t1) and not (ar.is_haraka(t1[m + 1])) and t1[m + 1] != ar.BEH and t1[m + 1] != ar.MEEM:
                self.declare(izhar_shafawi(a='True'))
                print(t1[m - 1: m + 5])
                ss = t1[m - 1: m + 5]
                result.append("الحكم اظهار شفوي" + '(' + ss + ')')

    @Rule()
    def findmadleem(self):
        t1 = ar.strip_shadda(t)
        a1 = []
        w1 = []
        y1 = []
        for i, char in enumerate(t1):
            if char == ar.ALEF:
                a1.append(i)
            if char == ar.WAW:
                w1.append(i)
            if char == ar.YEH:
                y1.append(i)
        for a in a1:
            if a > 0 and t1[a - 1] == ar.FATHA:
                self.declare(mad_alleen(a='True'))
                print(t1[a - 2: a + 1])
                ss=t1[a - 2: a + 1]
                result.append("الحكم مد اللين"+'('+ss+')')
        for w in w1:
            if w > 0 and t1[w - 1] == ar.FATHA:
                self.declare(mad_alleen(a='True'))
                print(t1[w - 2: w + 1])
                ss = t1[w - 2: w + 1]
                result.append("الحكم مد اللين" + '(' + ss + ')')
        for y in y1:
            if y > 0 and t1[y - 1] == ar.FATHA:
                self.declare(mad_alleen(a='True'))
                print(t1[y - 2: y + 1])
                ss = t1[y - 2: y + 1]
                result.append("الحكم مد اللين" + '(' + ss + ')')

    @Rule()
    def findmad_wajeb_motasel(self):
        t1 = ar.strip_shadda(t)
        a1 = []
        w1 = []
        y1 = []
        for i, char in enumerate(t1):
            if char == ar.ALEF:
                a1.append(i)
            if char == ar.WAW:
                w1.append(i)
            if char == ar.YEH:
                y1.append(i)
        for a in a1:
            if a > 0 and t1[a - 1] == ar.FATHA:
                if a + 1 < len(t1) and ar.is_hamza(t1[a + 1]):
                    self.declare(mad_wajeb_motasel(a='True'))
                    print(t1[a - 2: a + 2])
                    ss=t1[a - 2: a + 2]
                    result.append("الحكم مد واجب متصل"+'('+ss+')')
        for w in w1:
            if w > 0 and t1[w - 1] == ar.DAMMA:
                if w + 1 < len(t1) and ar.is_hamza(t1[w + 1]):
                    self.declare(mad_wajeb_motasel(a='True'))
                    print(t1[w - 2: w + 2])
                    ss = t1[w - 2: w + 2]
                    result.append("الحكم مد واجب متصل" + '(' + ss + ')')
        for y in y1:
            if y > 0 and t1[y - 1] == ar.KASRA:
                if y + 1 < len(t1) and ar.is_hamza(t1[y + 1]):
                    self.declare(mad_wajeb_motasel(a='True'))
                    print(t1[y - 2: y + 2])
                    ss = t1[y - 2: y + 2]
                    result.append("الحكم مد واجب متصل" + '(' + ss + ')')

    @Rule()
    def findmad_jaaez_monfasel(self):
        t1 = ar.strip_shadda(t)
        a1 = []
        w1 = []
        y1 = []
        for i, char in enumerate(t1):
            if char == ar.ALEF:
                a1.append(i)
            if char == ar.WAW:
                w1.append(i)
            if char == ar.YEH:
                y1.append(i)
        for a in a1:
            if a > 0 and t1[a - 1] == ar.FATHA:
                if a + 1 < len(t1) and t1[a + 1] == ' ':
                    if a + 2 < len(t1) and ar.is_hamza(t1[a + 2]):
                        self.declare(mad_jaaez_monfasel(a='True'))
                        print(t1[a - 2: a + 3])
                        ss=t1[a - 2: a + 3]
                        result.append("الحكم مد جائز منفصل"+'('+ss+')')
        for w in w1:
            if w > 0 and t1[w - 1] == ar.DAMMA:
                if w + 1 < len(t1) and t1[w + 1] == ' ':
                    if w + 2 < len(t1) and ar.is_hamza(t1[w + 2]):
                        self.declare(mad_jaaez_monfasel(a='True'))
                        print(t1[w - 2: w + 3])
                        ss = t1[w - 2: w + 3]
                        result.append("الحكم مد جائز منفصل" + '(' + ss + ')')
        for y in y1:
            if y > 0 and t1[y - 1] == ar.KASRA:
                if y + 1 < len(t1) and t1[y + 1] == ' ':
                    if y + 2 < len(t1) and ar.is_hamza(t1[y + 2]):
                        self.declare(mad_jaaez_monfasel(a='True'))
                        print(t1[y - 2: y + 3])
                        ss = t1[y - 2: y + 3]
                        result.append("الحكم مد جائز منفصل" + '(' + ss + ')')

    @Rule()
    def findmad_lazem_kaleme_mothqal(self):
        a1 = []
        w1 = []
        y1 = []
        for i, char in enumerate(t):
            if char == ar.ALEF:
                a1.append(i)
            if char == ar.WAW:
                w1.append(i)
            if char == ar.YEH:
                y1.append(i)
        for a in a1:
            if a > 0 and t[a - 1] == ar.FATHA:
                if a + 2 < len(t) and ar.is_shadda(t[a + 2]):
                    self.declare(mad_lazem_kaleme_mothqal(a='True'))
                    print(t[a - 3: a + 3])
                    ss=t[a - 3: a + 3]
                    result.append("الحكم مد لازم كلمي مثقل"+'('+ss+')')
        for w in w1:
            if w > 0 and (t[w - 1] == ar.DAMMA or t[w - 1] == ar.FATHA):
                if w + 2 < len(t) and ar.is_shadda(t[w + 2]):
                    self.declare(mad_lazem_kaleme_mothqal(a='True'))
                    print(t[w - 3: w + 3])
                    ss = t[w - 3: w + 3]
                    result.append("الحكم مد لازم كلمي مثقل"+'('+ss+')')
        for y in y1:
            if y > 0 and (t[y - 1] == ar.KASRA or t[y - 1] == ar.FATHA):
                if y + 2 < len(t) and ar.is_shadda(t[y + 2]):
                    self.declare(mad_lazem_kaleme_mothqal(a='True'))
                    print(t[y - 3: y + 3])
                    ss = t[y - 3: y + 3]
                    result.append("الحكم مد لازم كلمي مثقل"+'('+ss+')')

    @Rule()
    def findmad_lazem_kaleme_mokhafaf(self):
        a1 = []
        w1 = []
        y1 = []
        for i, char in enumerate(t):
            if char == ar.ALEF:
                a1.append(i)
            if char == ar.WAW:
                w1.append(i)
            if char == ar.YEH:
                y1.append(i)
        for a in a1:
            if a > 0 and t[a - 1] == ar.FATHA:
                if a + 2 < len(t) and ar.is_sukun(t[a + 2]):
                    self.declare(mad_lazem_kaleme_mokhafaf(a='True'))
                    print(t[a - 2: a + 3])
                    ss=t[a - 2: a + 3]
                    result.append("الحكم مد لازم كلمي مخفف"+'('+ss+')')
        for w in w1:
            if w > 0 and t[w - 1] == ar.DAMMA:
                if w + 2 < len(t) and ar.is_sukun(t[w + 2]):
                    self.declare(mad_lazem_kaleme_mokhafaf(a='True'))
                    print(t[w - 2: w + 3])
                    ss = t[w - 2: w + 3]
                    result.append("الحكم مد لازم كلمي مخفف" + '(' + ss + ')')
        for y in y1:
            if y > 0 and t[y - 1] == ar.KASRA:
                if y + 2 < len(t) and ar.is_sukun(t[y + 2]):
                    self.declare(mad_lazem_kaleme_mokhafaf(a='True'))
                    print(t[y - 2: y + 3])
                    ss = t[y - 2: y + 3]
                    result.append("الحكم مد لازم كلمي مخفف" + '(' + ss + ')')

    @Rule(text(v=1))
    def findmad_lazem_harfi_mothqal(self):
        if s == 2 or s == 3 or s == 7 or s == 10 or s == 11 or s == 12 or s == 13 or s == 14 or s == 15 or s == 19 or s == 20 or s == 26 or s == 27 or s == 28 or s == 29 or s == 30 or s == 31 or s == 32 or s == 36 or s == 38 or s == 40 or s == 41 or s == 42 or s == 43 or s == 44 or s == 45 or s == 46 or s == 50 or s == 68:
            sen = t.find(ar.SEEN)
            lam = t.find(ar.LAM)
            if sen != -1:
                if t[sen + 1] == ar.YEH or t[sen + 1] == ar.REH or t[sen + 1] == ar.MEEM or t[sen + 1] == ar.LAM or t[
                    sen + 1] == ar.WAW or t[sen + 1] == ar.NOON:
                    self.declare(mad_lazem_harfi_mothqal(a='True'))
                    print(t[sen: sen + 2])
                    ss=t[sen: sen + 2]
                    result.append("الحكم مد لازم حرفي مثقل"+'('+ss+')')
            if lam != -1:
                if t[lam + 1] == ar.MEEM:
                    self.declare(mad_lazem_harfi_mothqal(a='True'))
                    print(t[lam: lam + 2])
                    ss = t[lam: lam + 2]
                    result.append("الحكم مد لازم حرفي مثقل"+'('+ss+')')

    @Rule(text(v=1))
    def findmad_lazem_harfi_mokhafaf(self):
        if s == 2 or s == 3 or s == 7 or s == 10 or s == 11 or s == 12 or s == 13 or s == 14 or s == 15 or s == 19 or s == 20 or s == 26 or s == 27 or s == 28 or s == 29 or s == 30 or s == 31 or s == 32 or s == 36 or s == 38 or s == 40 or s == 41 or s == 42 or s == 43 or s == 44 or s == 45 or s == 46 or s == 50 or s == 68:
            self.declare(mad_lazem_harfi_mokhafaf(a='True'))
            f = t.find(' ')
            if f != -1:
                print(t[f - 1])
                ss=t[f-1]
                result.append("الحكم مد لازم حرفي مخفف"+'('+ss+')')
            else:
                print(t[len(t) - 1])
                ss=t[len(t)-1]
                result.append("الحكم مد لازم حرفي مخفف"+'('+ss+')')


'''
engine = ES()
engine.reset()
engine.run()
'''